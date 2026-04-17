import requests

response = requests.post(
    "http://localhost:5000/api/profiles",
    json={"name": "Rasheed"}
)

print(response.status_code)
print(response.json())