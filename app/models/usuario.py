class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento

    def atualizar_dados(self, novo_nome, novo_email, novo_data_nascimento):
        self.nome = novo_nome
        self.email = novo_email
        self.data_nascimento = novo_data_nascimento