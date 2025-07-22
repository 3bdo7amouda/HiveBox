#!/usr/bin/env python3
"""
HiveBox Flask Application

Main Flask application for HiveBox environmental sensor data tracking.
Provides RESTful API endpoints for version info and sensor data.
"""

import logging
import re
from datetime import datetime

import requests
from flask import Flask, jsonify, request

__version__ = "0.1.2"

# Create Flask app instance
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SenseBox IDs from your configuration
SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c"
]

# openSenseMap API base URL
OPENSENSEMAP_BASE_URL = "https://api.opensensemap.org"


def validate_sensebox_id(sensebox_id):
    """
    Validate senseBox ID format and existence in allowed list.

    Args:
        sensebox_id (str): The ID to validate

    Returns:
        tuple: (is_valid, error_message)
    """
    if not sensebox_id:
        return False, "SenseBox ID cannot be empty"

    # Check if ID matches expected format (24 character hex string)
    if not re.match(r'^[a-fA-F0-9]{24}$', sensebox_id):
        return False, ("Invalid senseBox ID format. "
                       "Must be 24 character hexadecimal string")

    # Check if ID is in allowed list
    if sensebox_id not in SENSEBOX_IDS:
        return False, f"SenseBox ID not found in allowed list: {SENSEBOX_IDS}"

    return True, None


def fetch_sensebox_data(sensebox_id):
    """
    Fetch data from openSenseMap API for a specific senseBox.

    Args:
        sensebox_id (str): The ID of the senseBox

    Returns:
        tuple: (data, status_code, error_message)
    """
    try:
        url = f"{OPENSENSEMAP_BASE_URL}/boxes/{sensebox_id}"
        logger.info("Fetching data from: %s", url)

        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return None, 404, f"SenseBox {sensebox_id} not found"
        elif response.status_code == 429:
            return None, 429, "Rate limit exceeded. Please try again later"
        elif response.status_code >= 500:
            return None, 502, "openSenseMap service is temporarily unavailable"

        response.raise_for_status()
        return response.json(), 200, None

    except requests.exceptions.Timeout:
        return None, 504, "Request timeout - openSenseMap service is slow"
    except requests.exceptions.ConnectionError:
        return None, 503, "Cannot connect to openSenseMap service"
    except requests.exceptions.RequestException as e:
        logger.error("Error fetching data for senseBox %s: %s", sensebox_id, e)
        return None, 500, f"Failed to fetch data: {str(e)}"


def fetch_latest_measurements(sensebox_id):
    """
    Fetch latest measurements for all sensors of a senseBox.

    Args:
        sensebox_id (str): The ID of the senseBox

    Returns:
        tuple: (data, status_code, error_message)
    """
    try:
        url = f"{OPENSENSEMAP_BASE_URL}/boxes/{sensebox_id}/sensors"
        logger.info("Fetching latest measurements from: %s", url)

        response = requests.get(url, timeout=10)

        if response.status_code == 404:
            return None, 404, f"Sensors for senseBox {sensebox_id} not found"
        elif response.status_code == 429:
            return None, 429, "Rate limit exceeded. Please try again later"
        elif response.status_code >= 500:
            return None, 502, "openSenseMap service is temporarily unavailable"

        response.raise_for_status()
        return response.json(), 200, None

    except requests.exceptions.Timeout:
        return None, 504, "Request timeout - openSenseMap service is slow"
    except requests.exceptions.ConnectionError:
        return None, 503, "Cannot connect to openSenseMap service"
    except requests.exceptions.RequestException as e:
        logger.error("Error fetching measurements for senseBox %s: %s",
                     sensebox_id, e)
        return None, 500, f"Failed to fetch measurements: {str(e)}"


def get_temperature_from_sensebox(sensebox_data, latest_measurements):
    """
    Extract temperature data from senseBox response and measurements.

    Args:
        sensebox_data (dict): Response from openSenseMap API
        latest_measurements (dict): Latest measurements from sensors endpoint

    Returns:
        dict: Temperature data or None if not found
    """
    if not sensebox_data or 'sensors' not in sensebox_data:
        return None

    # Look for temperature sensor with more flexible matching
    temperature_keywords = [
        'temperature', 'temperatur', 'temp', 'température',
        'lufttemperatur', 'air temperature', 'ambient temperature'
    ]

    for sensor in sensebox_data['sensors']:
        phenomenon = sensor.get('phenomenon', '').lower()
        unit = sensor.get('unit', '').lower()
        sensor_id = sensor.get('_id')

        # Check if phenomenon contains temperature keywords
        if any(keyword in phenomenon for keyword in temperature_keywords):
            # Get latest measurement from measurements endpoint
            measurement_value = None
            measurement_timestamp = None

            if latest_measurements and 'sensors' in latest_measurements:
                for measurement_sensor in latest_measurements['sensors']:
                    if measurement_sensor.get('_id') == sensor_id:
                        if 'lastMeasurement' in measurement_sensor:
                            measurement = measurement_sensor['lastMeasurement']
                            measurement_value = measurement.get('value')
                            measurement_timestamp = measurement.get('createdAt')
                        break

            return {
                'sensor_id': sensor_id,
                'phenomenon': sensor.get('phenomenon'),
                'unit': sensor.get('unit'),
                'value': measurement_value,
                'timestamp': measurement_timestamp
            }

        # Also check if unit indicates temperature (°C, celsius, etc.)
        if unit in ['°c', 'c', 'celsius', '°f', 'f', 'fahrenheit']:
            # Get latest measurement
            measurement_value = None
            measurement_timestamp = None

            if latest_measurements and 'sensors' in latest_measurements:
                for measurement_sensor in latest_measurements['sensors']:
                    if measurement_sensor.get('_id') == sensor_id:
                        if 'lastMeasurement' in measurement_sensor:
                            measurement = measurement_sensor['lastMeasurement']
                            measurement_value = measurement.get('value')
                            measurement_timestamp = measurement.get('createdAt')
                        break

            return {
                'sensor_id': sensor_id,
                'phenomenon': sensor.get('phenomenon'),
                'unit': sensor.get('unit'),
                'value': measurement_value,
                'timestamp': measurement_timestamp
            }

    return None


# Error handlers for common HTTP errors
@app.errorhandler(404)
def not_found(_):
    """Handle 404 errors."""
    return jsonify({
        "error": "Not Found",
        "message": "The requested resource was not found",
        "status": 404
    }), 404


@app.errorhandler(400)
def bad_request(_):
    """Handle 400 errors."""
    return jsonify({
        "error": "Bad Request",
        "message": "The request was invalid",
        "status": 400
    }), 400


@app.errorhandler(500)
def internal_error(_):
    """Handle 500 errors."""
    return jsonify({
        "error": "Internal Server Error",
        "message": "An internal server error occurred",
        "status": 500
    }), 500


@app.route('/version', methods=['GET'])
def get_version():
    """Return the current application version."""
    return jsonify({
        "version": __version__,
        "app": "HiveBox"
    })


@app.route('/', methods=['GET'])
def home():
    """Root endpoint with basic info."""
    return jsonify({
        "message": "Welcome to HiveBox API",
        "version": __version__,
        "endpoints": [
            "/version",
            "/temperature"
        ]
    })


@app.route('/temperature', methods=['GET'])
def get_temperature():
    """
    Get temperature data from configured senseBoxes.

    Query Parameters:
        - sensebox_id (optional): Specific senseBox ID to query

    Returns:
        JSON response with temperature data
    """
    # Get optional sensebox_id from query parameters
    requested_sensebox_id = request.args.get('sensebox_id')

    # Determine which senseBoxes to query
    if requested_sensebox_id:
        # Validate the requested senseBox ID
        is_valid, error_message = validate_sensebox_id(requested_sensebox_id)
        if not is_valid:
            return jsonify({
                "error": "Invalid senseBox ID",
                "message": error_message,
                "valid_ids": SENSEBOX_IDS
            }), 400

        sensebox_ids_to_query = [requested_sensebox_id]
    else:
        sensebox_ids_to_query = SENSEBOX_IDS

    results = []
    has_errors = False

    for sensebox_id in sensebox_ids_to_query:
        logger.info("Processing senseBox: %s", sensebox_id)

        # Fetch basic senseBox data
        sensebox_data, status_code, error_message = fetch_sensebox_data(
            sensebox_id)

        if sensebox_data is None:
            has_errors = True
            results.append({
                "sensebox_id": sensebox_id,
                "status": "error",
                "error_code": status_code,
                "message": error_message
            })
            continue

        # Fetch latest measurements
        latest_measurements, measurements_status, measurements_error = (
            fetch_latest_measurements(sensebox_id))

        if latest_measurements is None:
            has_errors = True
            results.append({
                "sensebox_id": sensebox_id,
                "status": "error",
                "error_code": measurements_status,
                "message": f"Failed to fetch measurements: {measurements_error}"
            })
            continue

        # Extract temperature data
        temperature_data = get_temperature_from_sensebox(
            sensebox_data, latest_measurements)

        if temperature_data is None:
            has_errors = True
            results.append({
                "sensebox_id": sensebox_id,
                "status": "error",
                "error_code": 404,
                "message": "No temperature sensor found"
            })
            continue

        # Add location info if available
        location = sensebox_data.get('currentLocation', {})

        results.append({
            "sensebox_id": sensebox_id,
            "status": "success",
            "name": sensebox_data.get('name', 'Unknown'),
            "location": {
                "coordinates": location.get('coordinates', []),
                "type": location.get('type', 'Point')
            },
            "temperature": temperature_data
        })

    # Determine appropriate HTTP status code
    if not results:
        status_code = 500
    elif has_errors and len([r for r in results if r['status'] == 'success']) == 0:
        # All requests failed
        status_code = 502
    elif has_errors:
        # Partial success
        status_code = 207  # Multi-status
    else:
        # All successful
        status_code = 200

    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_results": len(results),
        "successful_results": len([r for r in results if r['status'] == 'success']),
        "failed_results": len([r for r in results if r['status'] == 'error']),
        "data": results
    }), status_code


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
