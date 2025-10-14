'''
Crie um programa que leia quanto de dinheiro um pessoa tem na carteira e mostre
quantos dólares ela pode comprar.

Considere
US$1.00 = R$3.27
'''
carteira = float(input('Digite o valor em carteira: R$'))
dolar = carteira / 3.27
print('Como R${:.2f} você pode compra US${:.2f} dolares.'.format(carteira, dolar))
