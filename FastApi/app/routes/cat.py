from fastapi import APIRouter, Body
from models.cat_schema import Cat
from database import CatModel

cat_route = APIRouter()

@cat_route.post("/")
def create_cats(cat: Cat = Body(...)):
    CatModel.create(name=cat.name, gender=cat.gender, age=cat.age)
    return {"message": "Cat created successfully"}
    
@cat_route.get("/")
def read_cats():
    return [{"name": "ludwin"}, {"agender": "masculine"}]

@cat_route.get("/{id}")
def read_cats(id: int):
    return {"id": id}

@cat_route.put("/{id}")
def update_cats(id: int, cat: Cat = Body(...)):
    return cat

@cat_route.get("/{gender}")
def read_event(gender: str):
    return {"gender": gender}