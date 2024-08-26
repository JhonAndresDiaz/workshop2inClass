from fastapi import APIRouter, Body
from models.table_schema import Table
from database import TableModel

table_route = APIRouter()

@table_route.post("/")
def create_tables(table: Table = Body(...)):
    TableModel.create(color=table.color, size=table.size, numberPeople=table.numberPeople)
    return {"message": "Table created successfully"}

@table_route.get("/")
def get_tables():
    table = TableModel.select().where(TableModel.id > 0).dicts()
    return list(table)

@table_route.get("/{table_id}")
def get_table(table_id: int):
    try:
        table = TableModel.get(TableModel.id == table_id)
        return table
    except TableModel.DoesNotExist:
        return {"error": "Table not found"}
    