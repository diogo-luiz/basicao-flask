import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "video/1", {"name":"Video","likes": 10})
print(response.json())