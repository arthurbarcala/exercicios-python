from functions.cadastrar_user import cadastrar_user
from store_users.users import users

def generate_signup_user() -> None:
    print("--------------------------------------------")
    nome = input(f"Insira o primeiro nome do usuário a ser cadastrado:\n")
    sobrenome = input(f"Insira o sobrenome do usuário a ser cadastrado:\n")
    res_signup = cadastrar_user(nome=nome, sobrenome=sobrenome)
    
    if not res_signup:
        print("Tente novamente! Não foi possível realizar o cadastro...")
        print("(dica: o nome e sobrenome devem ter mais de 3 letras)")
        print("--------------------------------------------")
    else:
        print("Cadastro realizado com sucesso!")
        print("--------------------------------------------")