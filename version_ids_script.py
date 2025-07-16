#!/usr/bin/env python3
"""
HiveBox Application - Version and SenseBox IDs Script

This module provides basic functionality for the HiveBox application including
version printing and SenseBox ID management for environmental sensor data tracking.
"""

__version__ = "0.0.1"

def print_version():
    """Print the current application version and exit."""
    print(f"HiveBox v{__version__}")
    exit(0)

# SenseBox IDs for future use
SENSEBOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488", 
    "5ade1acf223bd80019a1011c"
]

def get_sensebox_ids():
    """Return the list of senseBox IDs."""
    return SENSEBOX_IDS

if __name__ == "__main__":
    print_version()
