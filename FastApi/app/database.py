from dotenv import load_dotenv
from peewee import *
import os

load_dotenv()

database = MySQLDatabase(
    os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT'))
)

class UserModel(Model):
    id = AutoField(primary_key = True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password =CharField(max_length=50)

    class Meta:
        database = database
        table_name = "users"

class TableModel(Model):
    id = AutoField(primary_key = True)
    color = CharField(max_length=20)
    size = CharField(max_length=20)
    numberPeople =CharField(max_length=10)

    class Meta:
        database = database
        table_name = "tables"