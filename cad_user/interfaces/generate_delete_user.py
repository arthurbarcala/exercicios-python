from functions.kill_user import kill_user
from functions.buscar_user import buscar_user

def generate_delete_user() -> None:
    print("----------------------------")
    cod = str(input(f"Digite o código do usuário a ser deletado:\n"))
    
    if buscar_user(cod=cod) != None:
        option = str(input(f"Tem certeza que deseja deletar {buscar_user(cod=cod)['nome_completo']}? [Y|n]\n")).lower()
        
        if option == 'y':
            print(f"{buscar_user(cod=cod)['nome_completo']} foi deletado com sucesso!")
            kill_user(cod=cod)
        else:
            print("Processo de exclusão cancelado!")
    else:
        print("O usuário não existe!")
    
    