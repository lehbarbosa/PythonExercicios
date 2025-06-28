"""
Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será
a base da conversão:

- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""
num_decimal = int(input('Informe um número inteiro: '))
print("""Escolha qual será a base de conversão:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")
opcao = int(input('Digite a opção: '))

if opcao == 1:
    print(f'O número {num_decimal} na base Binário é {bin(num_decimal)[2:]}')
elif opcao == 2:
    print(f'O número {num_decimal} na base Octal é {oct(num_decimal)[2:]}')
elif opcao == 3:
    print(f'O número {num_decimal} na base Hexadecimal é {hex(num_decimal)[2:].upper()}')
else:
    print('Opção inválida. Por favor, escolha apenas 1, 2 ou 3.')
