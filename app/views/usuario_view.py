from colorama import init, Fore, Style

init(autoreset=True)

class Usuario_terminal_view:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE USUARIOS (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadastrar usuário")
        print(f"2 - Listar usuário")
        print(f"3 - Atualizar usuário")
        print(f"4 - Excluir usuário")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_usuario(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE USUARIO ===")
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        return nome, email, data_nascimento
    
    def ler_id(self):
        try: 
            return int(input("Digite o ID do usuário: "))
        except ValueError:
            return -1
        
    def exibir_usuarios(self, usuarios):
        print(Fore.YELLOW + "\n--- TABELA DE USUARIOS ---")
        if not usuarios:
            print("Nenhum usuário cadastrado")
            return
        
        print(f"{'ID' :<4} | {'NOME' :<20} | {'EMAIL' :<20} | {'DATA DE NASCIMENTO' :<10}")
        print("-"*50)
        for u in usuarios:
            print(f"{u.id :<4} | {u.nome :<20} | {u.email :<20} | {u.data_nascimento :<10}")
        print("-"*50)

    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")