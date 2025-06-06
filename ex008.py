# Escreva um programa que leia um valor em metros e o exiba convertido
# em centímetros e em milímetros.

valor = float(input('Digite o valor em metros: '))

cent = valor * 100
mili = valor * 1000

print('O valor {} m -> {} cm'.format(valor, cent))
print('O valor {} m -> {} mm'.format(valor, mili))
