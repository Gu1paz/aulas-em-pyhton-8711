from datetime import datetime, date

class Data_Utils:

    FORMATO_DATA = "%d/%m/%Y"

    @staticmethod #recebo data string e converte para data(mês, dia ou ano)
    def string_para_data(data):
        return datetime.strfptime(data, Data_Utils.FORMATO_DATA).data()
    
    @staticmethod #nesse caso seria ao contrario quero transformar a data em string
    def data_para_string(data):
        return data.strftime(Data_Utils.FORMATO_DATA)
    
    @staticmethod
    def validar_data(data):
        try:
            datetime.strftime(data, Data_Utils.FORMATO_DATA)
            return True
        except ValueError:
            return False
        
    @staticmethod
    def calcular_idade(data):
        data_inicio = Data_Utils.string_para_data(data)
        hoje = date.today()
        idade = hoje.year - data_inicio.year
        if(hoje.month, hoje.day) < (data_inicio.month, data_inicio.day):
            idade -= 1
        return idade     
