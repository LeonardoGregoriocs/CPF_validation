from db.database import DB


database = DB()


class Queries:
    def __init__(self) -> None:
        pass

    def create_table(self):
        cursor = database.cursor()

        cursor.execute(
        """CREATE TABLE IF NOT EXISTS base_teste(
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

        database.commit()

    def insert_data(self, data):
        cursor = database.cursor()

        sql = """
            INSERT INTO
                base_teste
            (
                cpf,
                private,
                incompleto,
                data_ultima_compra,
                ticket_medio,
                ticket_ultima_compra,
                loja_mais_frequente,
                loja_ultima_compra
            ) VALUES (
                %(cpf)s,
                %(private)s,
                %(incompleto)s,
                %(data_ultima_compra)s,
                %(ticket_medio)s,
                %(ticket_ultima_compra)s,
                %(loja_mais_frequente)s,
                %(loja_ultima_compra)s
            )
        """

        cursor.execute(sql, {
            'cpf': data['cpf'],
            'private': data['private'],
            'incompleto': data['incompleto'],
            'data_ultima_compra': data['data_ultima_compra'],
            'ticket_medio': data['ticket_medio'],
            'ticket_ultima_compra': data['ticket_ultima_compra'],
            'loja_mais_frequente': data['loja_mais_frequente'],
            'loja_ultima_compra': data['loja_ultima_compra']
        })

        database.commit()
