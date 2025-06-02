dinheiro = float(input('Digite quanto de dinheiro tem em carteira: R$'))

dolar: float = dinheiro / 3.27
print('Como esse dinheiro você pode compra US${:.2f}.\n'.format(dolar))
