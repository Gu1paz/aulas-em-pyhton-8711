class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self._id = id
        self._razao_social = razao_social
        self._nome_fantasia = nome_fantasia
        self._cnpj = cnpj
        self._sla_atendimento = sla_atendimento
        
        

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id

    @property
    def razao_social(self):
        return self._razao_social
    
    @razao_social.setter
    def razao_social(self, novo_razao_socail):
        self._razao_social = novo_razao_socail

    @property
    def nome_fantasia(self):
        return self._nome_fantasia
    
    @nome_fantasia.setter
    def nome_fantasia(self, novo_nome_fantasia):
        self._nome_fantasia = novo_nome_fantasia

    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    @property
    def sla_atendimento(self):
        return self._sla_atendimento
    
    @sla_atendimento.setter
    def sla_atendimento(self, novo_sla_atendimento):
        self._sla_atendimento = novo_sla_atendimento
    

    def validar_sla(self):  # Remova o 'sla_atendimento' daqui
        if self.sla_atendimento < 0:  # Adicione 'self.' antes de sla_atendimento
            raise ValueError("Erro: Não é permitido SLA negativo!!!")
        
    def atualizar_dados(self, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.sla_atendimento = sla_atendimento

        self.validar_sla()
        