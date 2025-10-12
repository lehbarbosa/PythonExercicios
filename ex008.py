'''
Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.
'''
valor = int(input('Digite o valor em metros: '))
cent = valor * 100
mili = valor * 1000
print('O valor {}m convertido para centímetros é {}cm'.format(valor, cent))
print('O valor {}m convertido para milímetros é {}mm'.format(valor, mili))
