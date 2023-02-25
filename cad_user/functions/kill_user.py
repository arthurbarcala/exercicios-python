from store_users.users import users
from functions.buscar_user import buscar_user

def kill_user(cod:str) -> bool:
    user_found = buscar_user(cod=cod)
    
    for y in users:
            if user_found["codigo"] == y["codigo"]:
                users.remove(y)