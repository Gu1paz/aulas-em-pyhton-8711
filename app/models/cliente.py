from app.core.data_utils import Data_Utils

class Cliente:
    def __init__(self, id, nome, data_nascimento, limite_credito):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.limite_credito = limite_credito

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, novo_data_nascimento):
        self._data_nascimento = novo_data_nascimento

    @property
    def limite_credito(self):
        return self._limite_credito

    @limite_credito.setter
    def limite_credito(self, novo_limite_credito):
        self._limite_credito = novo_limite_credito


    def validar_limite_credito(self):
        if self.limite_credito < 0:
            raise ValueError("Erro: Não é permitido limite negativo!!!")
        
    @property
    def idade(self):
        return Data_Utils.calcular_idade(self._data_nascimento)
        
    def atualizar_dados(self, novo_nome, novo_data_nascimento, novo_limite_credito):
        self.nome = novo_nome
        self.data_nascimento = novo_data_nascimento
        self.limite_credito = novo_limite_credito