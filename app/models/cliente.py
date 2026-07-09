class Cliente:
    def __init__(self, id, nome, data_nascimento, limite_credito):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.limite_credito = limite_credito

    def validar_limite_credito(self):
        if self.limite_credito < 0:
            raise ValueError("Erro: Não é permitido limite negativo!!!")
        
    def atualizar_dados(self, novo_nome, novo_data_nascimento, novo_limite_credito):
        self.nome = novo_nome
        self.data_nascimento = novo_data_nascimento
        self.limite_credito = novo_limite_credito