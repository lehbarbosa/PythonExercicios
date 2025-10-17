'''
Faça um programa que leia o ângulo qualquer e mostre na tela o valor do seno,
cosseno e tangente desse ângulo.
'''
import math
ang = float(input("Digite um ângulo: "))
seno = math.sin(math.radians(ang))
print("O ângulo de {} tem SENO de {:.2f}".format(ang, seno))
cosseno = math.cos(math.radians(ang))
print("O ângulo de {} tem COSSENO de {:.2f}".format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print("O ângulo de {} tem TANGENTE de {:.2f}".format(ang, tangente))