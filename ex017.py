from math import sqrt
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

hipo = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

print('O valor da hipotenusa é: {:.2f}'.format(hipo))
