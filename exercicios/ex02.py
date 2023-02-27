def main():
    array = []
    arraySort = []
    while True:
        num = input(f"Digite um número:\n")
        
        try:
            num = int(num)
            array.append(num)
            print(f"{num} foi adicionado na lista")
            
        except:
            print("É pra digitar um NÚMERO, seu animal!!!!")
            
        r = input(f"Deseja continuar? (sim|nao)\n").lower()
        
        if(r == "nao"):
            break
        
    for i in array:
        if i not in arraySort:
            arraySort.append(i)
    arraySort.sort()
    print(f"A lista ficou: {arraySort}")
    print(f"O menor numero: {arraySort[0]}")
    print(f"O maior numero: {arraySort[len(arraySort)-1]}")
    print(f"A soma da array ficou: {sum(arraySort)}")
    
if __name__ == "__main__":
    main()