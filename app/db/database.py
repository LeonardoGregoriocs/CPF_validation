import psycopg2

class DB:
    def __init__(self) -> None:
        pass

    def connect():
        connection = psycopg2.connect(
            database="dataclient",
            host="172.18.0.2",
            user="neowayuser",
            password="neoway"
        )

        cursor = connection.cursor()

        # cursor.execute(
        # """CREATE TABLE base_teste(
        #     cpf varchar(11) NOT NULL,
        #     PRIMARY KEY (cpf),
        #     private smallint NULL,
        #     incompleto smallint NULL,
        #     data_ultima_compra varchar(10) NULL,
        #     ticket_medio float NULL,
        #     ticket_ultima_compra float NULL,
        #     loja_mais_frequente varchar(14) NULL,
        #     loja_ultima_compra varchar(14) NULL);
        #     """
        # )

        connection.commit()

        return cursor
