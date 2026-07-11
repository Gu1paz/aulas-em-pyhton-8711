class Usuario:
    def __init__(self, id, nome, email, data_nascimento):
        self.id = id
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento

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
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @data_nascimento.setter
    def data_nascimento(self, novo_data_nascimento):
        self._data_nascimento = novo_data_nascimento

    def atualizar_dados(self, novo_nome, novo_email, novo_data_nascimento):
        self.nome = novo_nome
        self.email = novo_email
        self.data_nascimento = novo_data_nascimento