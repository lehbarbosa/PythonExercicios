# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

from math import sin, cos, tan

ang = float(input('Digite um ângulo para ver seu [seno, cosseno e tangente]: '))
print('O seno do ângulo {} é: {:.3f}'.format(ang, sin(ang)))
print('O cosseno do ângulo {} é: {:.3f}'.format(ang, cos(ang)))
print('O tangente do ângulo {} é: {:.3f}'.format(ang, tan(ang)))
