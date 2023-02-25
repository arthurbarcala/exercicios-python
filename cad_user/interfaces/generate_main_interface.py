from interfaces.generate_signup_user import generate_signup_user
from interfaces.generate_delete_user import generate_delete_user
from interfaces.generate_search_user import generate_search_user
from interfaces.generate_list_users import generate_list_users
from interfaces.generate_qt_registers import generate_qt_registers

def generate_main_interface() -> None:
    available_options = ['C', 'D', 'B', 'L', 'Q', 'K']
    
    print("Olá, seja bem vindo ao cadastro de usuários da Germinare Tech!")
    print("---------------------------------------------")
    
    while(True):
        print(f"O que deseja fazer?\n")
        selection = str(input(f"[C] Cadastrar Usuário | [D] Deletar Usuário | [B] Buscar Usuário | [L] Listar todos os usuários | [Q] Verificar quantidade de registros | [K] Encerrar o programa\n")).upper()
        
        if selection not in available_options:
            print("Desculpe, esta opção é inválida!")
        elif selection == 'C':
            generate_signup_user()
        elif selection == 'D':
            generate_delete_user()
        elif selection == 'B':
            generate_search_user()
        elif selection == 'L':
            generate_list_users()
        elif selection == 'Q':
            generate_qt_registers()
        elif selection == 'K':
            break