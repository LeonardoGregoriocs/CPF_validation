import psycopg2

class DB:
    def __init__(self) -> None:
        self.connection = psycopg2.connect(
            database="dataclient",
            host="172.18.0.2",
            user="neowayuser",
            password="neoway"
        )

    def cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def commit(self):
        return self.connection.commit()
