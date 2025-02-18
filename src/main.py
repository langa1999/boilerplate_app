from typing import Optional
import pymongo
from fastapi import FastAPI
import requests

app = FastAPI()


client = pymongo.MongoClient('mongodb', 27017)
db = client['my_db']
collection = db['nobel_prizes']


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/load_data")
def load_data():
    response = requests.get('https://api.nobelprize.org/v1/prize.json')
    response.raise_for_status()
    data = response.json()
    collection.drop()
    collection.insert_many(data['prizes'])
    print("Data successfully ingested into MongoDB.")


@app.get("/search_name")
def search_name(name: Optional[str] = None):
    if name:
        query = {"laureates.firstname": {"$regex": f"^{name.replace(' ', '.*').replace('-', '.*')}", "$options": "i"}}
        results = collection.find(query, {"_id": 0})
        return list(results)
    return {"error": "No name provided"}
