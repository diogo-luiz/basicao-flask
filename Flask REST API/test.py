import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 2, "name": "Dio", "views": 101230000},
        {"likes": 3, "name": "Diow", "views": 1030000},
        {"likes": 10, "name": "Di", "views": 100000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)

input()
response = requests.get(BASE + "video/2")
print(response.json())

input()
response = requests.patch(BASE + "video/2", {'views':99, 'likes': 10239})
print(response.json())