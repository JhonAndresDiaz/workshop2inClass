from fastapi import APIRouter, Body
from models.shirt_schema import Shirt
from database import ShirtModel

shirt_route = APIRouter()

@shirt_route.post("/")
def create_shirts(shirt: Shirt = Body(...)):
    ShirtModel.create(design=shirt.design, color=shirt.color, typeGarment=shirt.typeGarment, size=shirt.size)
    return {"message": "Shirt created successfully"}
    
@shirt_route.get("/")
def read_shirts():
    return [{"desing": "unic"}, {"color": "green"}]

@shirt_route.get("/{id}")
def read_shirts(id: int):
    return {"id": id}

@shirt_route.put("/{id}")
def update_shirts(id: int, shirt: Shirt = Body(...)):
    return shirt

@shirt_route.get("/{desing}")
def read_event(desing: str):
    return {"desing": desing}