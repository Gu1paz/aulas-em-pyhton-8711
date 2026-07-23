from colorama import init, Fore, Style 

init(autoreset=True)

class Produto_Terminal_View:
    def __init__(self):
        self.titulo_sistema = "=== CRUD DE PRODUTOS (MVC) ==="

    def renderizar_menu(self):
        print(Fore.CYAN + Style.BRIGHT + self.titulo_sistema)
        print(f"1 - Cadstrar produto")
        print(f"2 - Listar produtos")
        print(f"3 - Atualizar produto")
        print(f"4 - Excluir produto")
        print(f"0 - Sair")
        print(Fore.CYAN + "="*50)
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1
        
    def ler_dados_produto(self):
        print(Fore.CYAN + Style.BRIGHT + "=== CADASTRO DE PRODUTO ===")
        nome = input("Digite o nome do produto: ")
        estoque = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
        return nome, estoque, preco
    
    def ler_id(self):
        return input("Digite o ID do produto: ")
    
    def exibir_fornecedores(self, fornecedores):
        print(Fore.YELLOW + "\n--- FORNECEDORES DISPONÍVEIS ---")
        print(f"{'ID':<4} | {'NOME FANTASIA':<30}") 
        print("-"* 40)
        for fornecedor in fornecedores:
            print(
                f"{fornecedor.id:<4} | {fornecedor.nome_fantasia:<30}"
            )
        print("-"* 40)

    def ler_fornecedor(self, fornecedor_existente = None):
        if fornecedor_existente is None:
            return input("Informe o ID do fornecedor: ")
        valor = input(
            f"Fornecedor [{Fore.GREEN}{fornecedor_existente}{Style.RESET_ALL}]: "
        )
        if valor == "":
            return fornecedor_existente
        return valor
    
    def exibir_produtos(self, produtos):
        print(Fore.YELLOW + "\n--- TABELA DE PRODUTOS ---")
        if not produtos:
            print("Nenhum produto cadastrado")
            return
        print(f"{'ID' :<4} | {'NOME' :<20} | {'ESTOQUE' :<7} | {'PREÇO' :<10} | {'VALOR EM ESTOQUE' :<16} | {'FORNECEDOR':<10}")
        print("-"* 83)
        for p in produtos:
            print(f"{p.id :<4} | {p.nome :<20} | {p.estoque :<7} | {p.preco :<10.2f} | {p.valor_estoque :<16.2f} | {p.fornecedor.nome_fantasia :<10}")
        print("-"* 83)

    def exibir_mensagem(self, mensagem, sucesso=True):
        cor = Fore.GREEN if sucesso else Fore.RED
        print(cor + f"\n[STATUS] {mensagem}\n")
        self.aguardar_entrada()

    def aguardar_entrada(self):
        input(Fore.WHITE + "Pressione Enter para continuar...")