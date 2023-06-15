import time

from db.queries import Queries
from service.analyze_data_service import AnalyzeDataService


try:
    time.sleep(15)

    queries = Queries()
    queries.create_table()

    cpf_validation = AnalyzeDataService()
    cpf_validation.analyze_data()

    print("Script run successfully")

except Exception as err:
    print(f"Err: {err}")
