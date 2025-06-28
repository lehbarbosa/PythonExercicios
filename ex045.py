"""
Crie um programa que faça o computador jogar 
JOKENPÔ com você.
"""
from time import sleep
from random import randint
item = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
escolha_pc = item[computador]

print('=-=' * 20)
print(f'{"Vamos Jogar JOKENPÔ":^50}')
print('=-=' * 20)

print("""Escolha uma opção:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura""")
opcao = int(input('Qual vai ser sua jogada: '))
escolha_usu = item[opcao]

sleep(1)
print('JO',  end=' * ')
sleep(1)
print('KEN', end=' * ')
sleep(1)
print('PÔ')

print('-=' * 15)
print(f'Computador => {item[computador]}.')
print(f'Usuário => {item[opcao]}.')
print('-=' * 15)

# PEDRA
if computador == 0:
    if opcao == 0:
        print('Não houve ganhador!')
    elif opcao == 1:
        print('Você Ganhou!')
    elif opcao == 2:
        print('Computador Ganhou.')
    else:
        print('Jogada inválda!')
# Papel
elif computador == 1:
    if opcao == 0:
        print('Computador Ganhou!')
    elif opcao == 1:
        print('Não houve ganhador!')
    elif opcao == 2:
        print('Você ganhou')
    else:
        print('Jogada inválda!')

# Tesoura
elif computador == 2:
    if opcao == 0:
        print('Você Ganhou!')
    elif opcao == 1:
        print('Computador ganhou!')
    elif opcao == 2:
        print('Não houve ganhador')
    else:
        print('Jogada inválda!')
