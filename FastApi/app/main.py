from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from routes.user import user_route
from routes.table import table_route

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()

    try:
        yield
    
    finally:
        if not connection.is_closed():
            connection.close

app = FastAPI(lifespan = lifespan)

app.include_router(user_route, prefix="/api/users", tags={"users"})
app.include_router(table_route, prefix="/api/tables", tags={"tables"})