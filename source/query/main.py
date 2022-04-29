from fastapi import FastAPI

# Instantiate the app
app = FastAPI()

# Define a GET on the specified endpoint
@app.get("/")
async def say_hello():
    return {"greeting":"Hello World!"}

# A GET that in this case just returns the item_id we pass, 
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

# Note, parameters not declared in the path are automatically query parameters.