from flask import Flask, request

app = Flask(__name__)

stores = [{"name": "Bread Store", "items": [{"name": "Tea Bread", "price": 11.22}]}]


@app.get("/store")  # when we access this address, we run the below function
def get_store():
    return {"store": stores}


# to test if an API is working, we make requests and expect responses
# we test with observationsal or automated testing
# we would be using Insomnia rest client


# we then create a post request
@app.post("/store")
def post_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return (
        new_store,
        201,
    )  # status code 201 means "ive accepted the data and im ready to create"


# we want to give Bread Store another item after checking if that store is found
@app.post("/store/<string:name>/items")
def create_item(name):
    request_data = request.get_json()
    for new in stores:
        if new["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            new["items"].append(new_item)
            return (new_item, 201)
    return {"message": "store not found"}, 404


# get a particular store and its items
@app.get("/store/<string:name>")
def retrive_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "store does not exist"}, 404


# get items from a particular store
@app.get("/store/<string:name>/items")
def retrieve_store_items(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "no items to show, no store of that name"}, 404
