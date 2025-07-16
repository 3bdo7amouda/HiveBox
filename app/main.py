#!/usr/bin/env python3
"""
HiveBox Flask Application

Main Flask application for HiveBox environmental sensor data tracking.
Provides RESTful API endpoints for version info and sensor data.
"""

from flask import Flask, jsonify, request
import requests
import logging
from datetime import datetime

__version__ = "0.0.1"

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

def fetch_sensebox_data(sensebox_id):
    """
    Fetch data from openSenseMap API for a specific senseBox.
    
    Args:
        sensebox_id (str): The ID of the senseBox
        
    Returns:
        dict: Response data or None if failed
    """
    try:
        url = f"{OPENSENSEMAP_BASE_URL}/boxes/{sensebox_id}"
        logger.info(f"Fetching data from: {url}")
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises exception for bad status codes
        
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data for senseBox {sensebox_id}: {e}")
        return None

def fetch_latest_measurements(sensebox_id):
    """
    Fetch latest measurements for all sensors of a senseBox.
    
    Args:
        sensebox_id (str): The ID of the senseBox
        
    Returns:
        dict: Response data or None if failed
    """
    try:
        url = f"{OPENSENSEMAP_BASE_URL}/boxes/{sensebox_id}/sensors"
        logger.info(f"Fetching latest measurements from: {url}")
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching measurements for senseBox {sensebox_id}: {e}")
        return None

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
        if requested_sensebox_id not in SENSEBOX_IDS:
            return jsonify({
                "error": "Invalid senseBox ID",
                "valid_ids": SENSEBOX_IDS
            }), 400
        sensebox_ids_to_query = [requested_sensebox_id]
    else:
        sensebox_ids_to_query = SENSEBOX_IDS
    
    results = []
    
    for sensebox_id in sensebox_ids_to_query:
        logger.info(f"Processing senseBox: {sensebox_id}")
        
        # Fetch basic senseBox data
        sensebox_data = fetch_sensebox_data(sensebox_id)
        
        if sensebox_data is None:
            results.append({
                "sensebox_id": sensebox_id,
                "status": "error",
                "message": "Failed to fetch data from openSenseMap"
            })
            continue
        
        # Fetch latest measurements
        latest_measurements = fetch_latest_measurements(sensebox_id)
        
        # Extract temperature data
        temperature_data = get_temperature_from_sensebox(sensebox_data, latest_measurements)
        
        if temperature_data is None:
            results.append({
                "sensebox_id": sensebox_id,
                "status": "error",
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
    
    return jsonify({
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "total_results": len(results),
        "data": results
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)