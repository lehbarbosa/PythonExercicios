'''
Exercício Python 59:
Crie um programa que leia dois valores e mostre um menu na 
tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realziar a operção solicitada em cada 
caso.
'''
from time import sleep
from os import system

valor1 = float(input('Digito o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print(
        '[ 1 ] Somar\n'
        '[ 2 ] Multiplicar\n'
        '[ 3 ] Maior\n'
        '[ 4 ] Novos números\n'
        '[ 5 ] Sair do programa')
    opcao = int(input('Qual sua opção: '))
    if opcao == 1:
        system('cls')
        somar = valor1 + valor2
        print('\033[32mA soma entre: {:.0f} + {:.0f} = {:.0f}\033[m'.format(valor1, valor2, somar))
    elif opcao == 2:
        system('cls')
        multiplicacao = valor1 * valor2
        print('\033[32mA multiplicação entre: {:.0f} * {:.0f} = {:.0f}\033[m'.format(valor1, valor2, multiplicacao))
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        system('cls')
        print('\033[32mEntre {:.0f} e {:.0f} o maior é {:.0f}\033[m'.format(valor1, valor2, maior))
    elif opcao == 4:
        system('cls')
        print('Informe os valores novamente.')
        valor1 = float(input('Digito o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))  
    elif opcao == 5:
        sair = 5
        print('Saindo...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')