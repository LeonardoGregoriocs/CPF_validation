import time

time.sleep(10)

from db.queries import Queries
from service.analyze_data_service import AnalyzeDataService


try:
    queries = Queries()
    queries.create_table()

    analyze_data_service = AnalyzeDataService()
    analyze_data_service.analyze_data()

    print("Script run successfully")

except Exception as err:
    print(f"Err: {err}")
