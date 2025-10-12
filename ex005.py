'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e
seu antecessor.
'''
num = int(input('Digite um valor: '))
print('O sucessor de {} é {} e'.format(num, num + 1), end=' ')
print('o antercessor de {} é {}'.format(num, num - 1))
