"""
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela um mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))

if valor_1 > valor_2:
    print('O primeiro valor é MAIOR.')
elif valor_2 > valor_1:
    print('O seugndo valor é MAIOR.')
else:
    print('Não existe valor MAIOR, os dois são iguais')
    