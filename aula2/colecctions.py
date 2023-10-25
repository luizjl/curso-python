
# Lista

aluno = ['Luiz', 42, 1.65, True, [5,6,7,9]]

print("|" + "="*50 + "|")

print(aluno)

print("|" + "="*50 + "|")

aluno.append('Aprovado')

print(aluno[4][3])

print("|" + "="*50 + "|")

# Dictionary (json)
aluno_Luiz = {
    'nome': 'Luiz',
    'sobrenome': 'Lemos',
    'idade': 42,
    'peso': 65,
    'altura': 1.65,
    'notas':{
        '1': 9,
        '2':8.5,
        3: 10,
        4: 7
    }
}

nome = aluno_Luiz['nome']
sobrenome = aluno_Luiz.get('sobrenome')

print("|" + "="*50 + "|")

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")

print("|" + "="*50 + "|")

print(aluno_Luiz.items())
# dict_items([('nome', 'Luiz'), ('sobrenome', 'Lemos'), ('idade', 42), ('peso', 65), ('altura', 1.65), ('notas', {'1': 9, '2': 8.5, 3: 10, 4: 7})])

# Lista - mutável
lista = [1,2,3] 

# Tupla - imutável - não aceita alterar o valor
tupla = (1,2,3) 

lista[0] = 10 # Ok 
# tupla[0] = 10 -- TypeError: 'tuple' object does not support item assignment

dias_semana = ('Seg', 'Ter', 'Qua', 'Qui', 'Sex' ,'Sab' 'Dom')
meses_ano = ('Janeiro', 'Fevereiro')

print(f"Meses: {meses_ano.index('Janeiro')}")
# print(f"# meses: {meses_ano.count()}")
