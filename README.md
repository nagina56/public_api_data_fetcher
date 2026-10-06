# 🔗 Public API Data Fetcher

A beginner-friendly Python project that fetches data from a public REST API and processes the JSON response.

## ✨ Features

* Fetch data from a public API
* Send GET requests using Python
* Handle JSON responses
* Extract useful information
* Display user data
* Handle API errors
* Test API requests using Postman

## 🛠️ Technologies Used

* Python
* Requests
* REST API
* JSON
* Postman

## 🌐 API Used

### JSONPlaceholder

```text
https://jsonplaceholder.typicode.com/users
```

## ⚙️ Installation

Install the required library:

```bash
pip install requests
```

## ▶️ How to Run

```bash
python main.py
```

## 💻 How It Works

The project sends a GET request to the public API and receives user information in JSON format.

```python
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
```

## 🧪 Testing with Postman

The API was first tested using Postman with a GET request.

```text
GET https://jsonplaceholder.typicode.com/users
```

After confirming the API response, the same endpoint was used in the Python project.

## 📊 Example Output

```text
Name: Leanne Graham
Email: Sincere@april.biz
------------------------------
Name: Ervin Howell
Email: Shanna@melissa.tv
------------------------------
Name: Clementine Bauch
Email: Nathan@yesenia.net
------------------------------
```

## 📚 What I Learned

* Working with REST APIs
* Sending GET requests
* Handling JSON data
* Using the Requests library
* Handling API errors
* Testing APIs with Postman
* Extracting data from JSON responses

## 🚀 Future Improvements

* Add user search
* Fetch users by ID
* Save data to JSON
* Export data to CSV
* Add a GUI
* Integrate more public APIs

## 👩‍💻 Author

**Nagina Azhar**

Python Learner | AI & Automation Enthusiast

