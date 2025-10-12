'''
Crie um programa que leia quanto de dinheiro um pessoa tem na carteira e mostre
quantos dólares ela pode comprar.

Considere
US$1.00 = R$3.27
'''
carteira = float(input('Digite o valor em carteira: R$'))
dolar = carteira / 5.53
print('Como o valor R${} você pode compra US${:.3f} dolares.'.format(carteira, dolar))
