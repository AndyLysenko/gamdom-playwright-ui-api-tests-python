"""
constants.py: This module defines the base URL and standard user credentials for accessing the Gamdom website.
"""

import os

# Define BASE_URL
BASE_URL = 'https://gamdom.com'

# Define user credentials, securely fetching the password from environment variables
STANDARD_USER = {
    'username': 'andy_lysenko',
    'password': os.getenv('STANDARD_USER_PASS')
}

# Ensure the password is set
# if not STANDARD_USER['password']:
#     raise ValueError("STANDARD_USER_PASS environment variable is not set")

# You can add other global constants here as needed