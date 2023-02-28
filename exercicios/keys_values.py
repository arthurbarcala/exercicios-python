def to_dict(array_keys:list, array_values:list) -> dict:
    dict_return = {}
    
    try:
        for x in range(0, len(array_keys)):
            dict_return[array_keys[x]] = array_values[x]
    
        return dict_return
    except:
        return None

def main():
    print(to_dict(["ten", "twenty"], [10]))

if __name__ == "__main__":
    main()