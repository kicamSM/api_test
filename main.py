from enum import Enum 
from typing import Union, Optional, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Category(Enum): 
    TOOLS = "tools"
    CONSUMABLES = "consumables"

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category
    # is_offer: Union[bool, None] = None
    
    # normally this would be a database 
    # !important if you indent this it doesnt work. Remember indentation when working with python is important
items = {
    0: Item(name="Hammer", price="9.99", count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price="5.99", count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price="1.99", count=100, id=2, category=Category.CONSUMABLES),
}

@app.get("/")
# def read_root():
    # return {"Hello": "World"}
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}

@app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#  return {"item_id": item_id, "q": q}

def query_item(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f"item with {item_id=} does not exist"
        )
    return items[item_id]

# Function parameters that are not path parameters can be speicified as query parameters 
# Here we can query items like this /items?count=20

# Selection = dict[
#     str, str | int | float | Category | None
# ] 

Selection = dict[str, Union[str, int, float, Category, Optional[Any]]]

# dictionary containing the user's query arguments 

@app.get("/items/")
def query_item_by_parameters(
    name: Optional[str] = None,
    # name: str | None = None, 
    price: Optional[float] = None, 
    count: Optional[int] = None, 
    category: Optional[Category] = None, 
    ) -> dict[str, Selection]:
    def check_item(item: Item) -> bool:
        return all(
            (
            name is None or item.name == name, 
            price is None or item.price == price, 
            count is None or item.count == count, 
            category is None or item.category is category
            )
        )
    selection = [item for item in items.values() if check_item(item)]
    print("testing print")
    # raise ValueError("testing valueError")
    return {
        "query": {"name": name, "price": price, "count": count, "category": category, "selection": selection, 
        }
    }

# send json to end point and then it will automatically return jsom data 
@app.post("/") 
def add_item(item: Item) -> dict[str, Item]: 
    
    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id} already exists")    
    
    # this adds items   
    # print("items[item.id]", items[item.id])
    # print(items)
    # raise KeyError("items:", items)
    # raise ValueError("items", items)
    items[item.id] = item
    # item[item.id] = item
    return {"added": item}
    
   

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.put("/update/{item_id}")
@app.put("/items/{item_id}")
# can also call /items/{item_id}
def update(
    item_id: int, 
    name: Optional[str] = None,
    price: Optional[float] = None, 
    count: Optional[int] = None, 
    ) -> dict[str, Selection]:
    
    print("update is being called")

    if item_id not in items: 
        HTTPException(status_code=404, detail=f"Item with {item_id} not found")
    if all(info is None for  info in (name, price, count)):
        raise HTTPException(status_code=400, detail="No parameters provided for update.")
    
@app.delete("/delete/{item_id}")
# can also call /items/{item_id}
def delete_item(item_id: int) -> dict [str, Item]:
    if item_id not in items: 
        raise HTTPException(
            status_code=404, detail=f"Item with {item_id} does not exist."
        )
    
    item = items.pop(item_id)
    return {"deleted": item}