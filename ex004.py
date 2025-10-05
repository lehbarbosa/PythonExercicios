'''
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
'''
n = input('Digite algo: ')
print(type(n))
print('É numerico: {}'.format(n.isalnum()))
print('Tem caractere alfabetico: {}'.format(n.isalpha()))
print('Convete caractere minuscula: {}'.format(n.islower()))
print('Convete caractere maiuscula: {}'.format(n.isupper()))
