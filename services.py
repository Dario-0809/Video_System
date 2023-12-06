import requests

BASE = "http://127.0.0.1:5000/"

# GET by ID
response = requests.get(BASE + "video/1")
print(response.json())
input()

# PUT by ID
response = requests.put(BASE + "video/5", {"name":"Nguyen Nam Anh", "views":1000, "likes": 100500})
print(response.json())
input()

# PATCH by ID
response = requests.patch(BASE + "video/1", {"name":"Dao Hai Long"})
print(response.json())
input()

# DELETE by ID
response = requests.delete(BASE + "video/5" )
print(response.json())

