"""
Unit tests for HiveBox Flask application.

Tests cover all endpoints, error scenarios, and API integrations.
"""

import json
import unittest
from unittest.mock import patch, MagicMock

import pytest

from app.main import app, validate_sensebox_id, SENSEBOX_IDS


class TestHiveBoxAPI(unittest.TestCase):
    """Test suite for HiveBox API endpoints."""

    def setUp(self):
        """Set up test client and configuration."""
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        
        # Sample test data
        self.valid_sensebox_id = "5eba5fbad46fb8001b799786"
        self.invalid_sensebox_id = "invalid_id"
        self.nonexistent_sensebox_id = "123456789012345678901234"
        
        # Mock sensebox data
        self.mock_sensebox_data = {
            "name": "Test SenseBox",
            "currentLocation": {
                "coordinates": [7.123456, 51.987654],
                "type": "Point"
            },
            "sensors": [
                {
                    "_id": "sensor123",
                    "phenomenon": "temperature",
                    "unit": "°C",
                    "lastMeasurement": {
                        "value": 22.5,
                        "createdAt": "2025-07-16T12:00:00Z"
                    }
                }
            ]
        }
        
        # Mock measurements data
        self.mock_measurements_data = {
            "sensors": [
                {
                    "_id": "sensor123",
                    "lastMeasurement": {
                        "value": 22.5,
                        "createdAt": "2025-07-16T12:00:00Z"
                    }
                }
            ]
        }

    def test_home_endpoint(self):
        """Test the home endpoint returns correct information."""
        response = self.client.get('/')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertEqual(data['message'], 'Welcome to HiveBox API')
        self.assertIn('version', data)
        self.assertIn('/version', data['endpoints'])
        self.assertIn('/temperature', data['endpoints'])

    def test_version_endpoint(self):
        """Test the version endpoint returns correct version information."""
        response = self.client.get('/version')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertIn('version', data)
        self.assertEqual(data['app'], 'HiveBox')

    def test_validate_sensebox_id_valid(self):
        """Test validation of valid senseBox ID."""
        is_valid, error_message = validate_sensebox_id(self.valid_sensebox_id)
        
        self.assertTrue(is_valid)
        self.assertIsNone(error_message)

    def test_validate_sensebox_id_empty(self):
        """Test validation of empty senseBox ID."""
        is_valid, error_message = validate_sensebox_id("")
        
        self.assertFalse(is_valid)
        self.assertEqual(error_message, "SenseBox ID cannot be empty")

    def test_validate_sensebox_id_invalid_format(self):
        """Test validation of invalid format senseBox ID."""
        is_valid, error_message = validate_sensebox_id("invalid_format")
        
        self.assertFalse(is_valid)
        self.assertIn("Invalid senseBox ID format", error_message)

    def test_validate_sensebox_id_not_in_list(self):
        """Test validation of senseBox ID not in allowed list."""
        is_valid, error_message = validate_sensebox_id(self.nonexistent_sensebox_id)
        
        self.assertFalse(is_valid)
        self.assertIn("not found in allowed list", error_message)

    @patch('app.main.fetch_sensebox_data')
    @patch('app.main.fetch_latest_measurements')
    def test_temperature_endpoint_success(self, mock_measurements, mock_sensebox):
        """Test successful temperature data retrieval."""
        # Mock successful API responses
        mock_sensebox.return_value = (self.mock_sensebox_data, 200, None)
        mock_measurements.return_value = (self.mock_measurements_data, 200, None)
        
        response = self.client.get('/temperature')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertIn('timestamp', data)
        self.assertEqual(data['total_results'], len(SENSEBOX_IDS))
        self.assertGreaterEqual(data['successful_results'], 0)
        self.assertIn('data', data)

    def test_temperature_endpoint_invalid_sensebox_id(self):
        """Test temperature endpoint with invalid senseBox ID."""
        response = self.client.get(f'/temperature?sensebox_id={self.invalid_sensebox_id}')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        
        self.assertEqual(data['error'], 'Invalid senseBox ID')
        self.assertIn('message', data)

    def test_404_error_handler(self):
        """Test 404 error handler."""
        response = self.client.get('/nonexistent-endpoint')
        
        self.assertEqual(response.status_code, 404)
        data = json.loads(response.data)
        
        self.assertEqual(data['error'], 'Not Found')
        self.assertEqual(data['status'], 404)


if __name__ == '__main__':
    unittest.main()