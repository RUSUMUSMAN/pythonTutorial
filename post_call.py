import requests

# The URL for the register POST request
url = "https://reqres.in/api/register"

header = {
    "x-api-key": "reqres-free-v1"
}

# Data to be sent in the request body
data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

# Making the POST request
response = requests.post(url, headers=header, data=data)

# Checking if the request was successful
if response.status_code == 200:
    print("User registered successfully!")
    print(f"Response: {response.json()}")
else:
    print(response.text)
    print(f"Failed to register user. Status code: {response.status_code}")
