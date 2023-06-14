from .database import DB

cursor = DB.connect()

class Queries:
    def __init__(self) -> None:
        pass

    def create_table(self):
        cursor.execute(
        """CREATE TABLE base_teste
            cpf serial NOT NULL,
            PRIMARY KEY (cpf,
            private smallint NULL,
            incompleto smallint NULL,
            data_ultima_compra text(10) NULL,
            ticket_medio double precision NULL,
            ticket_ultima_compra double precision NULL,
            loja_mais_frequente integer(14) NULL,
            loja_ultima_compra integer(14) NULL;"""
        )

    def insert_data(self):
        cursor.execute(
            "INSERT INTO"
        )
