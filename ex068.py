'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele 
conquistou no final do jogo.
'''
from random import randint
computador = randint(1, 10)
while True:
    num = int(input('Digite um valor: '))
    jogador = str(input('PAR ou ÍMPAR? [P/I] ')).strip().upper()
# print('-' * 50)
# print(f'Você jogou {num} e o computador {computador}. Total de {...} DEU {...}')
# print('-' * 50)
# print(f'Você PERDEU!')
# print('-=' * 50)
# print(f'GAME OVER! Você venceu {...} vezes.')
