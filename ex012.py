'''
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
'''
valor_produto = float(input('Digite o valor do produto: R$'))
valor_desconto = valor_produto - (valor_produto * (5 / 100)) 
print('O produto que custava R${}, na promoção com desconto de 5% vai custa R${:.2f}'.format(valor_produto, valor_desconto))
