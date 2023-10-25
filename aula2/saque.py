"""
Laboratório 02 - Página 117
    
    Suponha que em um caixa eletrônico existam cédulas disponíveis de 5, 10, 20 e 50 reais. 
    Usando operações de divisão inteira e resto da divisão, escrever um programa que solicite ao usuário um valor para saque e, 
    a partir deste valor, armazenar em variáveis e apresentar na tela a quantidade de cada cédula para compor o valor do saque.
    
    Obs.: Considerar neste exercício que os valores sejam sempre múltiplos de 5. Considerar também a menor quantidade possível de cédulas.

"""

saque = int(input("Quanto você deseja sacar? [ Cédulas disponíveis: 5, 10, 20, 50 ] \n"))

qtd_cedulas_50 = saque // 50;
resto = saque % 50

qtd_cedulas_20 = resto // 20;
resto = resto % 20

qtd_cedulas_10 = resto // 10;
resto = resto % 10

qtd_cedulas_5 = resto // 5;

print("|" + "="*50 + "|")
print(f"Valor sacado: R$ {saque}")
print(f"Notas disponibilizadas")
print(f" > {qtd_cedulas_50} de R$ 50")
print(f" > {qtd_cedulas_20} de R$ 20")
print(f" > {qtd_cedulas_10} de R$ 10")
print(f" > {qtd_cedulas_5} de R$ 5")

print("|" + "="*50 + "|")