from fastapi import FastAPI

app = FastAPI()

local_storage = {}

@app.get("/")
def get_words():
	"""
	This endpoint gets the words from local storage.
	"""
	return {"message": [{k:v} for k,v in local_storage.items()]}

@app.post("/{word}")
def create_word(word: str):
	"""
	This endpoint creates a new word in local_storage.
	"""

	idx = len(local_storage.keys())

	local_storage[idx] = word

	return {"message": {idx: word}}

@app.put("/{word_id}/{word}")
def update_word(word_id: int, word: str):
	"""
	This endpoint updates an existing word in local_storage by word_id.
	"""

	if not local_storage.get(word_id):
		return {"message": "Word does not exist."}

	local_storage[word_id] = word

	return {"message": {word_id: word}}


@app.delete("/{word_id}")
def delete_word(word_id: int):
	"""
	This endpoint deletes a word from local storage.
	"""

	if word_id not in local_storage.keys():
		return {"message": "Word does not exist."}

	local_storage.pop(str(word_id), None)

	return {"message": "Deleted"}
