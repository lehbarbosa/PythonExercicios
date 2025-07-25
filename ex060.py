'''
Exercício Python 60: 
Faça um programa que leia um número qualquer e mostre o seu
fatorial.

Ex.: 
5!=5x4x3x2x1=120
'''
num = int(input('Digite um número para ver seu fatorial: '))
cont = 1
fatorial = num
while cont < num:
    fatorial *= num - cont
    cont += 1
print('O fatorial de {}! é {}'.format(num, fatorial))
