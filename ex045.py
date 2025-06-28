"""
Crie um programa que faça o computador jogar 
JOKENPÔ com você.
"""
from time import sleep
from random import choice
opcao_pc = choice(['Pedra', 'Papel', 'Tesoura'])

print('=-=' * 20)
print(f'{"Vamos Jogar JOKENPÔ":^50}')
print('=-=' * 20)

print("""Escolha uma opção:
[ 1 ] - Pedra
[ 2 ] - Papel
[ 3 ] - Tesoura""")
opcao = int(input('Qual vai ser sua jogada: '))

sleep(1)
print('JO',  end=' * ')
sleep(1)
print('KEN', end=' * ')
sleep(1)
print('PÔ')

# PEDRA
if opcao == 1:
    if opcao_pc == 'Pedra':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Pedra.')
        print('Não houve ganhador!')
    elif opcao_pc == 'Papel':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Pedra.')
        print('Ganhei!')
    elif opcao_pc == 'Tesoura':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Pedra.')
        print('Você GANHOU! Parabéns.')


# PAPEL
if opcao == 2:
    if opcao_pc == 'Pedra':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Papel.')
        print('Você GANHOU! Parabéns.')
    elif opcao_pc == 'Papel':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Papel.')
        print('Não houve ganhador!')
    elif opcao_pc == 'Tesoura':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Pedra.')
        print('Ganhei!')

# Tesoura
if opcao == 3:
    if opcao_pc == 'Pedra':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Tesoura.')
        print('GANHEI!')
    elif opcao_pc == 'Papel':
        print(f'Escolhei {opcao_pc}.')
        print('Você escolheu Tesoura.')
        print('Você GANHOU! Parabéns.')
    elif opcao_pc == 'Tesoura':
        print(f'Escolhe {opcao_pc}.')
        print('Você escolheu Tesoura.')
        print('Não houve ganhador. EMPATE!')
