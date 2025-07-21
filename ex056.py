"""
Exercício Python 56: 
    Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
    No final do programa, mostre: 
    > a média de idade do grupo, 
    > qual é o nome do homem mais velho 
    > quantas mulheres têm menos de 20 anos.
"""
soma_idade = 0
idade_maior = 0
nome_mais_velho = ''
cont_mulher_menor_20 = 0
for pes in range(1, 5):
    print(f'------- {pes}ª Pessoa -------')
    nome = str(input(f'Digite o nome: '))
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo [M/F]: ')).upper()
    # Calculo da média:
    soma_idade += idade
    media = soma_idade / pes
    # Calculo idade Homem mais velho:
    if sexo == 'M':
        if idade > idade_maior:
            idade_maior = idade
            nome_mais_velho = nome
    # Calculo idade Mulher menor de 20 anos:
    if sexo == 'F':
        if idade < 20:
            cont_mulher_menor_20 += 1
print()
print('=' * 30)
print(f'A média de idade do grupo é de \033[32m{media}\033[m')
print(f'O \033[33m{nome_mais_velho}\033[m é o homem mais velho com \033[33m{idade_maior} anos.\033[m')
print(f'Temos \033[35m{cont_mulher_menor_20}\033[m mulher menores de 20 anos.')
