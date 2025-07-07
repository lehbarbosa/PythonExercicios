"""Crie um programa que leia uma frase qualquer e diga se ela é um 
palíndromo, desconsiderando os espaços.
Ex.:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
frase = str(input('Digite uma frase: ')).strip().upper()
frase_separada = frase.split()
junto = ''.join(frase_separada)
frase_invertida = ''

for palavra in range(len(junto) - 1, -1, -1):
    frase_invertida += junto[palavra]
    
print(F'O inverso de {junto} é {frase_invertida}')
if frase_invertida == junto:
    print('Temos um palíndromo!')
else:
    print('Frase NÃO É UM PALÍNDROMO!')
