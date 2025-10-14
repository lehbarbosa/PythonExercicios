'''
Escreva um programa que leia um valor em metros e o exiba convertido em
centímetros e milímetros.
'''
valor = int(input('Digite o valor em metros: '))
cent = valor * 100
mili = valor * 1000
print("A medida de {}m corresponde a:".format(valor))
print('{}cm'.format(cent))
print('{}mm'.format(mili))
