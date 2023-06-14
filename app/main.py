from fastapi import FastAPI

from .database.queries import Queries
from .service.analyze_data_service import AnalyzeData

app = FastAPI()


@app.get("/")
def index():
    queries = Queries()
    queries.create_table()

    cpf_validation = AnalyzeData()
    cpf_validation.analyze_data()
