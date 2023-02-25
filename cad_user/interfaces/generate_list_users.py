from functions.return_all_users import return_all_users

def generate_list_users() -> None:
    print("----------------------------------------------")
    print("Selecione uma opção:")
    option = input(f"1 - Ordem de Cadastro | 2 - Ordem Alfabética | 3 - Ordem de código\n")
    
    print(return_all_users(option=option))