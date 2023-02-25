from functions.buscar_user import buscar_user

def generate_search_user() -> None:
    while True:
        cod = input(f"Digite o código do usuário a ser buscado:\n")
        
        if buscar_user(cod=cod) != None:
            print("User encontrado:")
            print(f"Código: {buscar_user(cod=cod)['codigo']} - Nome: {buscar_user(cod=cod)['nome_completo']}")
        else:
            print("User não encontrado...")
            

        print('----------------------------------------------')
        
        escolha = str(input(f"Deseja buscar outro usuário? [Y|n]\n")).lower()
        
        if escolha != 'y':
            break
        
        