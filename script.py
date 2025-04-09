import requests
import json

# Define payload
payload = {
    'api_key': '7dfb4d3b4aa3d99fe3e2776e0b802d52',
    'url': 'https://www.deccanherald.com/',
    'render': 'true',
    'retry_404': 'true'
}

# Make the request
r = requests.get('https://api.scraperapi.com/', params=payload)

# Parse response
try:
    data = r.json()  # Convert JSON string to Python dictionary
    print(json.dumps(data, indent=4))  # Pretty print the JSON
except json.JSONDecodeError:
    print("Failed to parse JSON. Raw response:")
    print(r.text)
