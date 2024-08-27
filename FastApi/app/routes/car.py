from fastapi import APIRouter, Body
from models.car_schema import Car
from database import CarModel

car_route = APIRouter()

@car_route.post("/")
def create_cars(car: Car = Body(...)):
    CarModel.create(color=car.color, amount=car.amount, price=car.price, year=car.year)
    return {"message": "Car created successfully"}
    
@car_route.get("/")
def read_cars():
    return [{"color": "blue"}, {"amount": "four"}]

@car_route.get("/{id}")
def read_cars(id: int):
    return {"id": id}

@car_route.put("/{id}")
def update_cars(id: int, car: Car = Body(...)):
    return car

@car_route.get("/{amount}")
def read_event(amount: str):
    return {"amount": amount}