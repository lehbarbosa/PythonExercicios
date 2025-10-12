'''
Crie um algoritmo que leia um número e mostre o seu dobro,
triplo e raiz quadrada.
'''
num = int(input('Digite um valor para ver seu dobro, triplo e a raiz quadrada: '))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** (1/2)
print('O dobro de {} é {}'.format(num, dobro))
print('O triplo de {} é {}'.format(num, triplo))
print('O raiz quadra de {} é {:.3f}'.format(num, raiz_quadrada))
