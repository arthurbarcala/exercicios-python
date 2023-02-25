def inserir_lista(lista:list, val_vendas:float) -> list:
    comm = 200 + (0.09*val_vendas)
    
    if comm > 1000:
        pos = 8
    else:
        pos = int((comm/100)-2)
        
    lista[pos] +=1
    
    return lista
def main():
    lista = [0,0,0,0,0,0,0,0,0]
    while True:
        val_vendas = input(f"Qual o valor de vendas do funcionario?\n")
        try:
            val_vendas = float(val_vendas)
            lista = inserir_lista(lista=lista, val_vendas=val_vendas)
            
            comm = 200 + (0.09*val_vendas)
    
            if comm > 1000:
                pos = 8
            else:
                pos = int((comm/100)-2)
            
            print(f"O funcionário ganhou R${comm} de comissão e ficou na {pos+1}ª posição!")
            print("----")
            print("Quantidade de funcionários nas determinadas posições:")
            print(lista)
        except:
            if val_vendas == "sair":
                break
            else:
                print("Insira um valor válido!")
if __name__ == "__main__":
    main()