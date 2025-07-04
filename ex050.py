"""
Desenvolva um programa que leia seis números inteiros e mostre a 
soma apenas daqueles que forem pares. Se o valor digitado for ímpar, 
desconsidere-o.
"""
soma = 0
cont = 0 
for number in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(number)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} valores pares é {}'.format(cont, soma))
