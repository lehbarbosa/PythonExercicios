"""
Faça um programa que calcule a soma entre todos os números impares 
que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
print('*' * 50)
print(f'{"Contagem de Números Ímpares (1 a 500)":^50}')
print('*' * 50)

for impares in range(1, 501):
    if (impares % 2 == 1) and (impares / 3 == 0):
        impar = impares
        print(f'{impar}', end=' ')
