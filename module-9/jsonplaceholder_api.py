import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Connection Test")
print("Status Code:", response.status_code)
print()

print("Unformatted Response")
print(response.text)
print()

data = response.json()

print("Formatted Response")
print("Post ID:", data["id"])
print("User ID:", data["userId"])
print("Title:", data["title"])
print("Body:", data["body"])