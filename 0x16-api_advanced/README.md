# Python API Cheatsheet

## Introduction to APIs

- **API (Application Programming Interface)**: A set of rules and protocols that allows one software application to interact with another. APIs define the methods and data formats that applications can use to request and exchange information.

- **HTTP (Hypertext Transfer Protocol)**: The foundation of data communication on the internet. Most APIs use HTTP for communication.

- **HTTP Methods**:
  - `GET`: Retrieve data from the server.
  - `POST`: Send data to the server to create a new resource.
  - `PUT`: Send data to the server to update an existing resource.
  - `DELETE`: Request the removal of a resource.

## Making API Requests in Python

### Using the `requests` Library

```python
import requests

# Sending a GET request
response = requests.get(url)

# Sending a POST request with data
response = requests.post(url, data={"key": "value"})

# Sending a PUT request with JSON data
response = requests.put(url, json={"key": "value"})

# Sending a DELETE request
response = requests.delete(url)

# Handling JSON responses
data = response.json()

# Checking response status code
if response.status_code == 200:
    # Request was successful
else:
    # Handle errors


# Adding Headers

headers = {"User-Agent": "MyApp/1.0"}
response = requests.get(url, headers=headers)

# Query Parameters
params = {"param1": "value1", "param2": "value2"}
response = requests.get(url, params=params)

# Handling API Responses

- Response Status Codes:

* 200: OK (Successful request)
* 201: Created (Resource created)
* 204: No Content (Successful, but no response data)
* 400: Bad Request (Invalid request)
* 401: Unauthorized (Authentication required)
* 403: Forbidden (Access denied)
* 404: Not Found (Resource not found)
* 500: Internal Server Error (Server error)

- Response Data:

* response.text: Raw response data as text
* response.json(): Parsed JSON response data


# Authentication

import requests
from requests.auth import HTTPBasicAuth

username = "your_username"
password = "your_password"
url = "https://api.example.com/resource"

response = requests.get(url, auth=HTTPBasicAuth(username, password))