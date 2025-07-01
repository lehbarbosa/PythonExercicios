"""
Crie um programa que mostrer na tela todos os números pares que estão 
no intervalo entre 1 e 50.
"""
print('*' * 40)
print(f'{"Contagem de Números Pares (1 a 50)":^40}')
print('*' * 40)

print('Forma de resolução 1:')
for pares in range(1, 51):
    if pares % 2 == 0:
        par = pares
        print(f'{par}', end=' ')

# Forma de resolução 2:
print('\n')
print('Forma de resolução 2:')
for par in range(2, 51, 2):
    print(f'{par}', end=' ')