import psycopg2

class DB:
    def __init__(self) -> None:
        pass

    def connect():
        connection = psycopg2.connect(
            database="dataclient",
            host='database',
            user= 'neowayuser',
            password='neoway'
    )

        cursor = connection.cursor()
        return cursor
