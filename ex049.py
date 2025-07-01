"""
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário 
escolher, só que agora utilizando um laço For.
"""
print('*' * 40)
print(f'{"Tabuada usando Laço For":^40}')
print('*' * 40)

valor_inicio = int(input('\nDigite um número para ver a tabuada: '))
fim = int(input('Digite até que número deseja ver a tabuada: '))

print('*' * 20)
for c in range(1, fim + 1):
    print(f'{c} x {valor_inicio} = {c * valor_inicio}')
print('*' * 20)
