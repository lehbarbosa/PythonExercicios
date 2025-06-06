# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos
# separados.
# Ex.:
# >Digite um número: 1834
#     >unidade: 4
#     >dezena: 3
#     >centena: 8
#     >milhar: 1

num = int(input('DEntre com um número de 0 a 9999: '))
unidade = num // 1 % 10 
dezena = num // 10 % 10 
centena = num // 100 % 10 
milhar = num // 1000 % 10 

print('\nAnalisando o número {}'.format(num))
print('Unidade: {}'
      '\nDezena: {}'
      '\nCentena: {}'
      '\nMilhar: {}\n'.format(unidade, dezena, centena, milhar))
