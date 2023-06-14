from db.queries import Queries
from service.analyze_data_service import AnalyzeData


try:
    queries = Queries()
    queries.create_table()

    cpf_validation = AnalyzeData()
    cpf_validation.analyze_data()

except Exception as err:
    print(f"Err: {err}")