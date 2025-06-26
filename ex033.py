# Faça um programa que leia três números e mostre
# qual é o Maior e qual é o Menor.

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

# Verificando Menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

# Verificando Maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
