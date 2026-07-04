class Fornecedor:
    def __init__(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.sla_atendimento = sla_atendimento
        
        self.validar_sla()

    def validar_sla(self, sla_atendimento):
        if sla_atendimento < 0:
            raise ValueError("Erro: Não é permitido SLA negativo!!!")

    def atualizar_dados(self, id, razao_social, nome_fantasia, cnpj, sla_atendimento):
        self.id = id
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.sla_atendimento = sla_atendimento

        self.validar_sla()
        