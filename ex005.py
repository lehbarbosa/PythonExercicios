# Faça um programa que leia um número Inteiro e mostre na tela
# seu antecessor e seu sucessor.

num = int(input('Digite um valor: '))

antecessor = num - 1
sucessor = num + 1

print('O antecessor de {} é: {} '.format(num, antecessor))
print('E o sucessor de {} é: {} '.format(num, sucessor))