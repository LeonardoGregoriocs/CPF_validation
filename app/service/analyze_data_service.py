import pandas as pd
from validate_docbr import CPF, CNPJ

class AnalyzeData():
    def __init__(self) -> None:
        self.most_frequent_store_obj = None
        self.last_buy_obj = None

    def analyze_data(self):
        datas = pd.read_csv('./base_teste.txt', delim_whitespace=True)

        for data in datas.iterrows():
            cpf_obj = self.multipleReplace(data[1][0])
            cpf_is_valid = self.validator_cpf(cpf_obj)

            if not cpf_is_valid:
                continue

            if not pd.isna(data[1][6]):
                self.most_frequent_store_obj = self.multipleReplace(data[1][6])
                most_frequent_store_is_valid = self.validator_cnpj(self.most_frequent_store_obj)

                if not most_frequent_store_is_valid:
                    self.most_frequent_store_obj = None

            if not pd.isna(data[1][7]):
                self.last_buy_obj = self.multipleReplace(data[1][7])
                last_buy_is_valid = self.validator_cnpj(self.last_buy_obj)

                if not last_buy_is_valid:
                    self.last_buy_obj = None

            data_obj = {
                'CPF': cpf_obj,
                'PRIVATE': data[1][1],
                'INCOMPLETO': data[1][2],
                'DATA DA ULTIMA COMPRA': data[1][3],
                'TICKET MÉDIO': data[1][4],
                'TICKET DA ULTIMA COMPRA': data[1][5],
                'LOJA MAIS FREQUENTE': self.most_frequent_store_obj,
                'LOJA DA ULTIMA COMPRA': self.last_buy_obj
            }

            print(data_obj)

    def validator_cpf(self, cpf_text):
        cpf = CPF()
        cpf_is_valid = cpf.validate(cpf_text)

        if cpf_is_valid:
            return True
        return False

    def validator_cnpj(self, cnpj_text):
        cnpj = CNPJ()
        cnpj_is_valid = cnpj.validate(cnpj_text)

        if cnpj_is_valid:
            return True
        return False

    def multipleReplace(self, text):
        for char in ". - /":
            text = text.replace(char, "")
        return text