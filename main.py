import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    users = response.json()

    for user in users:
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print("-" * 30)

except requests.exceptions.RequestException as error:
    print(f"Error: {error}")