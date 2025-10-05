'''
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
'''
n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('Só tem espaços? ', n.isspace())
print('É um número: ',n.isnumeric())
print('É alfabetico: ',n.isalpha())
print('É alfanumerico: ', n.isalnum())
print('É minuscula: ', n.islower())
print('É maiuscula: ',n.isupper())
print('Esta capitalizada: ', n.istitle())
