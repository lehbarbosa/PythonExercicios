"""
Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela um mensagem:

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

valor_1 = float(input('Primeiro valor: '))
valor_2 = float(input('Segundo valor: '))

if valor_1 > valor_2:
    print('O primeiro valor é MAIOR.')
elif valor_2 > valor_1:
    print('O seugndo valor é MAIOR.')
elif valor_1 == valor_2:
    print('Não existe valor MAIOR, os dois são iguais')
else:
    print('Dados inválidos, apenas números.')
