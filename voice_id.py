import os
import requests

ELEVENLABS_API_KEY = 'sk_9864abac4ca3b9fefc8c0a5eb74464e31334cd4ed46903e6'

url = "https://api.elevenlabs.io/v1/voices"
headers = {"xi-api-key": ELEVENLABS_API_KEY}
response = requests.get(url, headers=headers)
print(response.json())  # This will print available voices with their IDs