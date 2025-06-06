# Crie um programa que leia quanto dinheiro a pessoa tem
# na carteria e mostre quantos Dólares ela pode comprar.

#     Considere:
#     US$1.00 = R$3,27

dinheiro = float(input('Digite quanto de dinheiro tem em carteira: R$'))

dolar: float = dinheiro / 3.27
print('Como esse dinheiro você pode compra US${:.2f}.\n'.format(dolar))
