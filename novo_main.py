import os
from colorama import init, Fore, Style

# Componentes de Fornecedores
from app.dao.fornecedor_dao import Fornecedor_DAO
from app.views.fornecedor_view import Fornecedor_terminal_view
from app.controllers.fornecedor_controller import Fornecedor_controller

class ErpApplication:
    def __init__(self):
        # Inicializa o colorama interno
        init(autoreset=True)
        
        # Inicialização centralizada dos ecossistemas (Container de Serviços manual)
        self._dao_produtos = Fornecedor_DAO()
        self._ctrl_produtos = Fornecedor_controller(dao=self._dao_produtos, view=Fornecedor_terminal_view())
        
        self._dao_fornecedores = Fornecedor_DAO()
        self._ctrl_fornecedores = Fornecedor_controller(dao=self._dao_fornecedores, view=Fornecedor_terminal_view())

    def _renderizar_menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + "=== SISTEMA CORPORATIVO ERP ===")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("0 - Sair do Sistema")
        print(Fore.GREEN + "==================================")
        try:
            return int(input("Escolha o módulo: "))
        except ValueError:
            return -1

    def run(self):
        while True:
            opcao = self._renderizar_menu_principal()
            
            if opcao == 0:
                print("\nEncerrando sistema corporativo...")
                break
            elif opcao == 1:
                self._ctrl_produtos.inicializar_sistema()
            elif opcao == 2:
                self._ctrl_fornecedores.inicializar_sistema()
            else:
                print(Fore.RED + "\nOpção inválida!")
                input(Fore.WHITE + "Pressione Enter para continuar...")


if __name__ == "__main__":
    app = ErpApplication()
    app.run()
    dao = Fornecedor_DAO()
    view = Fornecedor_terminal_view()
    controller = Fornecedor_controller(dao, view)
    controller.inicializar_sistema()