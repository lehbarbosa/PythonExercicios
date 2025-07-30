'''
Exercício Python 64: 
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, 
que é a condição de parada. No final, mostre quantos números 
foram digitados e qual foi o soma entre eles (desconsiderando o flag).
'''
print('Para cancelar digite 999')
num = totnum = soma = 0
while num != 999:
    num = int(input('Digite um número inteiro '))
    if num == 999:
        num = 999
    else:
        totnum += 1
        soma += num
print('Você digito um total de {} número'.format(totnum))
print('A soma de todos o valores digitado é {}'.format(soma))

