from .database.queries import Queries
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    queries = Queries()
    queries.create_table()