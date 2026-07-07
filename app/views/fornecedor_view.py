from colorama import init, Fore, Style

init(autoreset=True)

class Fornecedor_terminal_view:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE FORNECEDORES (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar fornecedor")
        print(f"2 - Listar fornecedores")
        print(f"3 - Atualizar fornecedor")
        print(f"4 - Excluir fornecedor")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def Ler_dados_fornecedor(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE FORNECEDOR ===")
        razao_social = input("Digite a Razão Social: ")
        nome_fantasia = input("Digite o Nome Fantasia: ")
        cnpj = input("Digite o CNPJ: ")
        try:
            sla_atendimento = int(input("Digite o SLA de atendimento (em dias): "))
        except ValueError:
            sla_atendimento = -1 # Força um valor inválido para o Model rejeitar na validação
            
        return razao_social, nome_fantasia, cnpj, sla_atendimento
    
    def ler_id(self):
        try:
            return int(input("Digite o ID do fornecedor: "))
        except ValueError:
            return -1
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- TABELA DE FORNECEDORES ---")
        if not fornecedores:
            print("Nenhum fornecedor cadastrado")
            return
        
        # Alinhando as colunas com os novos dados do quadro
        print(f"{'ID' :<4} | {'RAZÃO SOCIAL' :<20} | {'NOME FANTASIA' :<20} | {'CNPJ' :<15} | {'SLA' :<5}")
        print("-"*75)
        for f in fornecedores:
            # Acessando os atributos corretos do objeto Fornecedor (sem o underscore)
            print(f"{f.id :<4} | {f.razao_social :<20} | {f.nome_fantasia :<20} | {f.cnpj :<15} | {f.sla_atendimento :<5}")
        print("-"*75)

    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")