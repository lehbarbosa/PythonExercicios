"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi MAIOR e o MENOR peso lidos.
"""

print('\033[33m=\033[m' * 30)
print(f'\033[32m{"Lendo peso de 5 pessoas":^30}\033[m')
print('\033[33m=\033[m' * 30)

peso_maior = 0
peso_menor = 0
for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}ª: '))

    if pess == 1:
        peso_maior = peso
        peso_menor = peso
    else:
    # Verificando menor peso
        if peso > peso_maior:
            peso_maior = peso
    # Verificando menor peso
        if peso < peso_menor:
            peso_menor = peso

print(f'\033[33mO peso MAIOR foi de {peso_maior}kg\033[m')
print(f'\033[32mO peso MENOR foi de {peso_menor}kg\033[m')
