#!/usr/bin/env python3
"""
HiveBox Flask Application

Main Flask application for HiveBox environmental sensor data tracking.
Provides RESTful API endpoints for version info and sensor data.
"""

from flask import Flask, jsonify

__version__ = "0.0.1"

# Create Flask app instance
app = Flask(__name__)

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
            "/temperature (coming soon)"
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)