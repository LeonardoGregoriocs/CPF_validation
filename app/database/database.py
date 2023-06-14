import psycopg2

class DB:
    def __init__(self) -> None:
        pass

    def connect():
        connection = psycopg2.connect(
            database="dataclient",
            host="192.168.64.2",
            user="neowayuser",
            password="neoway"
        )

        cursor = connection.cursor()
        return cursor
