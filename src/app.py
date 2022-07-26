from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_items():
	return ['item1', 'item2']

@app.post("/{item_id}")
def create_item(item_id: int):
	return item_id

