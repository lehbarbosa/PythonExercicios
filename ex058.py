'''
Exercício Python 58:
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador  vai 
tentar adivinhar até acertar, mostrando no final quantos 
palpites foram necessários para vencer
'''
from random import randint
num_pc = randint(0, 10)
num_jogador = 0
cont_tentativas = 0
while num_jogador != num_pc:
    num_jogador = int(input('Em que número estou pensando? '))
    print('Processando...')
    print('Tente novamente!')
    cont_tentativas += 1

print('\033[32mPARABÉNS! \nVocê acertou o número que pensei foi {}\033[m'.format(num_pc))
print('\033[33mVocê preciso de {} tentativas\033[m'.format(cont_tentativas))
