from db.database import DB

cursor = DB.connect()

class Queries:
    def __init__(self) -> None:
        pass

    def create_table(self):
        cursor.execute(
        """CREATE TABLE base_teste(
            cpf varchar(11) NOT NULL,
            PRIMARY KEY (cpf),
            private smallint NULL,
            incompleto smallint NULL,
            data_ultima_compra varchar(10) NULL,
            ticket_medio float NULL,
            ticket_ultima_compra float NULL,
            loja_mais_frequente varchar(14) NULL,
            loja_ultima_compra varchar(14) NULL);
            """
        )

        cursor.commit()

    def insert_data(self):
        cursor.execute(
            "INSERT INTO"
        )
