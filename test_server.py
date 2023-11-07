import requests
# print(requests.get("http://127.0.0.1:8000/").json())
# print(requests.get("http://127.0.0.1:8000/items/0").json())
# print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

# # ! this is not working 
# print("***Adding an item:***")

print(
    requests.post(
    "http://127.0.0.1:8000/", 
    json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": "tools"}
    ).json()
)


# print(
#     requests.post(
#     "http://127.0.0.1:8000/", 
#     json=[{'name': 'Screwdriver', 'price': 3.99, 'count': 10, 'id': 4, 'category': 'tools'}]
#     ).json()
# )


# print("***Updating an item:***")

# print(requests.put("http://127.0.0.1:8000/items/0?count=9001").json())
# print(requests.get("http://127.0.0.1:8000/items/0").json())



# print("***Deleting an item:***")

# print(requests.put("http://127.0.0.1:8000/items/0").json())
# print(requests.get("http://127.0.0.1:8000/").json())
