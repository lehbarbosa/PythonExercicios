# Escreva um programa que faça o computador "pensar" em um 
# número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou
# perdeu.
import random
import time

num_pc = random.randint(0, 5)
print('Vou pensar num número entre 0 e 5 tente adivinhar...')
time.sleep(1)
num_usuario = int(input('Em que número estou pensando? '))
print('Processando...')
time.sleep(1)
if num_usuario == num_pc:
    print(f"PARABÉNS! Você venceu pensei no número {num_pc}")
else:
    print(f"GANHEI! Eu pensei no número {num_pc} e não no {num_usuario}!")