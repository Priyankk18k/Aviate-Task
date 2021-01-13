from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
app = FastAPI(debug=True)

class Item(BaseModel):
    timestamp: str
    email: str
    name: str
    city: str
    contact: int
    age: int
    recent_company: str
    role_in_company: str
    current_ctc: float
    fixed_component_ctc: float
    experience: float
    comfort: str
    relocate: str
    rate_english: int
    skills: str
    industries: str
    profile: str
    factors: str


@app.post("/items/insert/")
async def insert_data_mongo(item: Item):
        client = MongoClient('localhost', 27017)
        db = client.aviate_db
        collection = db.user_check
        data = db.user_check.find()
        dict_to_insert = {
            "timestamp": item.timestamp,
            "email": item.email,
            "name": item.name,
            "city": item.city,
            "contact": item.contact,
            "age": item.age,
            "recent_company": item.recent_company,
            "role_in_company": item.role_in_company,
            "current_ctc": item.current_ctc,
            "fixed_component_ctc": item.fixed_component_ctc,
            "experience": item.experience,
            "comfort": item.comfort,
            "relocate": item.relocate,
            "rate_english": item.rate_english,
            "skills": item.skills,
            "industries": item.industries,
            "profile": item.profile,
            "factors": item.factors

        }
        for i in data:
            if i['contact'] == item.contact:
                return "Item Already Present in the DB"
        result = collection.insert_one(dict_to_insert)
        return "Data Inserted in the DB Successfully :- {}".format(result)
