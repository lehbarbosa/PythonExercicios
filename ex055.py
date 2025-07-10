"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi MAIOR e o MENOR peso lidos.
"""
peso_maior = 0
peso_menor = 0
for pess in range(1, 6):
    peso = float(input(f'Digite o peso da {pess}ª: '))
    # Verificando maior peso
    peso_maior = peso
    if peso_maior >= peso and peso_maior < peso:
        peso_maior = peso
    # Verificando menor peso
    if peso_menor < peso_maior:
        peso_menor = peso

print(f'O peso MAIOR foi de {peso_maior}')
print(f'O peso MENOR foi de {peso_menor}')


