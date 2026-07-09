import os
from colorama import init, Fore, Style

# Componentes de Fornecedores

from app.dao.produto_dao import Produto_DAO
from app.views.produto_view import Produto_terminal_view
from app.controllers.produto_controller import Produto_controller

from app.dao.fornecedor_dao import Fornecedor_DAO
from app.views.fornecedor_view import Fornecedor_terminal_view
from app.controllers.fornecedor_controller import Fornecedor_controller

from app.dao.usuario_dao import Usuario_DAO
from app.views.usuario_view import Usuario_terminal_view
from app.controllers.usuario_controller import Usuario_controller

from app.dao.cliente_dao import Cliente_DAO
from app.views.cliente_view import Cliente_terminal_view
from app.controllers.cliente_controller import Cliente_controller


class ErpApplication:
    def __init__(self):
        # Inicializa o colorama interno
        init(autoreset=True)
        
        # Inicialização centralizada dos ecossistemas (Container de Serviços manual)
        self._dao_produtos = Produto_DAO()
        self._ctrl_produtos = Produto_controller(dao=self._dao_produtos, view=Produto_terminal_view())
        
        self._dao_fornecedores = Fornecedor_DAO()
        self._ctrl_fornecedores = Fornecedor_controller(dao=self._dao_fornecedores, view=Fornecedor_terminal_view())

        self._dao_usuarios = Usuario_DAO()
        self._ctrl_usuarios = Usuario_controller(dao=self._dao_usuarios, view=Usuario_terminal_view())

        self._dao_cliente = Cliente_DAO()
        self._ctrl_cliente = Cliente_controller(dao=self._dao_cliente, view=Cliente_terminal_view())


    def _renderizar_menu_principal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.GREEN + Style.BRIGHT + "=== SISTEMA CORPORATIVO ERP ===")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Fornecedores")
        print("3 - Gerenciar Usuários")
        print("4 - Gerenciar Clientes")
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
            elif opcao == 3:
                self._ctrl_usuarios.inicializar_sistema()
            elif opcao == 4:
                self._ctrl_cliente.inicializar_sistema()
            else:
                print(Fore.RED + "\nOpção inválida!")
                input(Fore.WHITE + "Pressione Enter para continuar...")


if __name__ == "__main__":
    app = ErpApplication()
    app.run()
    dao = Produto_DAO
    view = Produto_terminal_view
    controller = Produto_controller(dao, view)
    controller.inicializar_sistema()
    dao = Fornecedor_DAO()
    view = Fornecedor_terminal_view()
    controller = Fornecedor_controller(dao, view)
    controller.inicializar_sistema()
    dao = Usuario_DAO()
    view = Usuario_terminal_view()
    controller = Usuario_controller(dao, view)
    controller.inicializar_sistema()
    dao = Cliente_DAO()
    view = Cliente_terminal_view()
    controller = Cliente_controller(dao, view)
    controller.inicializar_sistema