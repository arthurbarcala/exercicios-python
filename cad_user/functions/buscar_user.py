from store_users.users import users

def buscar_user(cod:str) -> dict:
    for x in users:
        if x["codigo"] == cod:
            return x
            break
        else:
            return None
        