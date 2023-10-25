list = [1,2,3,5,6]

length = len(list)

for x in list:
    pass
    # print(x)
    
for x in range(0, 10, 3):
    pass
    # print(x)
    
for numero in range(6):
    pass
    # resto = numero % 20
    # if resto:
    #     print(f"Num: {num}")
    #     print(f"Numero: {numero}")
        

multiplo5 = False
tentativa = 1

while multiplo5 == False:
    saque = int(input("Digite um valor múltiplo de 5: "))
    
    if saque % 5 == 0:
        multiplo5 == True
    else:
        tentativa += 1
    
        if tentativa == 3:
            print("Inicie novamente o processo!!")
            break
        
        print("Valor não é múltiplo de 5, por favor tente novamente")

print(saque)
    