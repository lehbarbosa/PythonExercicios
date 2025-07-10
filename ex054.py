"""
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.
"""
from datetime import date
ano_atual = date.today().year
# ano_atual = 2017

cont_maior = 0
cont_menor = 0
for ano in range(1, 8):
    nascimento = int(input(f'Digite o ano da {ano}ª pessoa: '))
    if (ano_atual - nascimento) >= 18:
        cont_maior += 1
    else:
        cont_menor += 1

print('*' * 15)
print(f'\033[33m{cont_menor} pessoas NÃO ATIGIRAM A MAIORIDADE.\033[m')
print(f'\033[34m{cont_maior} pessoas ATINGIRAM A MAIORIDADE.\033[m')
print('*' * 15)
