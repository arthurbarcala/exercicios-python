def merge_dicts(dict_a:dict, dict_b:dict) -> dict:
    dict_ab = {}
    
    for x in dict_a:
        dict_ab[x] = dict_a[x]
    for x in dict_b:
        dict_ab[x] = dict_b[x]
    
    return dict_ab


def main():
    print(merge_dicts({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}))
    
if __name__ == "__main__":
    main()
            