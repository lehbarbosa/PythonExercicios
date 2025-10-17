'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triangulo ratangulo, calucle e mostre o comprimento da hipotenusa.
'''
from math import hypot
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
print("O comprimento da hipotenusa é igual: {:.2f}".format(hypot(cateto_oposto, cateto_adjacente)))
