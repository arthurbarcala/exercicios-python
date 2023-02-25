from store_users.users import users

def return_all_users(option:str) -> str:
    return_str:str = ""
    
    if option == '1':
        for x in users:
            return_str+=f"\nCódigo: {x['codigo']} - Nome: {x['nome_completo']}"
    elif option == '2':
        sorted_data = sorted(users, key=lambda d:d['nome_completo'])
        
        for x in sorted_data:
            return_str+=f"\nCódigo: {x['codigo']} - Nome: {x['nome_completo']}"
    elif option == '3':
        sorted_data = sorted(users, key=lambda d:d['codigo'])
        
        for x in sorted_data:
            return_str+=f"\nCódigo: {x['codigo']} - Nome: {x['nome_completo']}"
            
    return return_str