# API Authentication Testing

A Python-based API testing project using pytest and requests.
This project tests login functionality and protected API endpoints using the DummyJSON API.

## Features
- Successful login testing
- Invalid username and password testing
- Authentication token validation 
- Access without a token
- Access with an invalid token
- Reusable pytest fixtures

## Technologies
- Python
- Pytest
- Requests

## Run the tests
Install dependencies:

pip install -r requirements.txt

Run all tests:

python -m pytest -v