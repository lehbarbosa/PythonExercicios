'''
Exercício Python 58:
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador  vai 
tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer
'''
from random import randint
num_pc = randint(0, 10)
print('\033[33mSou seu computador... Acabei de pensar em um número entre 0 e 10.\033[m')
print('\033[33mSerá que você consegue adivinhar qual foi?\033[m')
num_jogador = 0
cont_tentativas = 0
while num_jogador != num_pc:
    num_jogador = int(input('Qual seu palpite? '))
    cont_tentativas += 1
    if num_jogador > num_pc:
        print('Menos... Tente mais uma vez.')
    elif num_jogador < num_pc:
        print('Mais... Tente mais uma vez.')
print('\033[32mAcertou com {} tentativas. PARABÉNS!\033[m'.format(cont_tentativas))
