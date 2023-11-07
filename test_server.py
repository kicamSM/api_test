import requests
import json
# print(requests.get("http://127.0.0.1:8000/").json())
# print(requests.get("http://127.0.0.1:8000/items/0").json())
# print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

# # ! this is working
# print("***Adding an item:***")

# print(
#     requests.post(
#     "http://127.0.0.1:8000/", 
#     json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 3, "category": "tools"}
#     ).json()
# )

# jsonfilepath = "./main.py"
# jsonfilepath = "/home/kicamsmm/Springboard_Recent/Springboard/test_api/main.py"
# print("***************************")
# print(json.loads(jsonfilepath))
# # * the file path is not working
# print("***************************")

# with open(jsonfilepath, "r") as p:
#     print(json.load(p))

st=""
print(json.loads(st))

# print("***Updating an item:***")
# print(json.loads(s))
print(requests.put("http://127.0.0.1:8000/items/0?count=9001").json())
print(requests.get("http://127.0.0.1:8000/items/0").json())



# print("***Deleting an item:***")

# print(requests.put("http://127.0.0.1:8000/items/3").json())
# print(requests.get("http://127.0.0.1:8000/").json())
