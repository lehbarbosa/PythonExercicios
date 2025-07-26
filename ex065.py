'''
Exercício Python 65: 
Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa
deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
sair = 'S'
media = 0
totvalor = 0
cont = 0
maior = None
menor = None
while sair != 'N':
    num = int(input('Digite um número inteiro: '))
    sair = str(input('Deseja continuar [S/N]: ')).strip().upper()
    
    totvalor += num
    cont += 1
    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num
media = totvalor / cont
print('A média dos valores digitados é {:.2f}'. format(media))
print('O MAIOR valor digitado é {}'. format(maior))
print('O MENOR valor digitado é {}'. format(menor))


