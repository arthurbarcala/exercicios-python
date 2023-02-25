from store_users.users import users
from random import randint
from functions.buscar_user import buscar_user

def cadastrar_user(nome:str, sobrenome:str) -> bool:
    if len(nome)<3 or len(sobrenome)<3:
        return False
        
        
    
    cod:str =  str(randint(1000, 9999))
    
    if buscar_user(cod=cod) != None:
        return False
    else:
        users.append(
            {
                "nome_completo":f"{nome.capitalize()} {sobrenome.capitalize()}",
                "codigo":cod,
            }
        )
        return True
    