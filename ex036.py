"""
Escreva um programa para aprovar o empréstimo bancário 
para a compra de um casa. O programa vai perguntar o 'o valor da casa', 
o 'salário' do comprador e em quantos anos ele vai pagar.

Calculer o valor da prestação mensal, sabendo que ele não 
pode exceder 30% do salário ou então o empréstimo será negado.
"""
print('\033[33m-=-\033[m' * 20)
print(f'\033[1;34m{"Digital Bank\033[m":^55}')
print('\033[33m-=-\033[m' * 20)

valor_casa = float(input('Informe o valor do imóvel: R$'))
salario = float(input('Informe o salário: R$'))
ano_parcelado = int(input('Informe em quantos anos será pago o empréstimo: '))

# Prestação mensal
prestacao_mensal = valor_casa / (ano_parcelado * 12)
valor_minimo_parcela = salario * (30 / 100)

if prestacao_mensal > valor_minimo_parcela:
    print(f'Para um emprétimo de \033[32mR${valor_casa:.2f}\033[m em {ano_parcelado} anos a prestação será de \033[34mR${prestacao_mensal:.2f}\033[m.')
    print('\033[31mEmpréstimo NEGADO!\033[m')
else:
    print(f'Para um emprétimo de \033[32mR${valor_casa:.2f}\033[m em {ano_parcelado} anos a prestação será de \033[34mR${prestacao_mensal:.2f}\033[m.')
    print('\033[32mEmpréstimo CONCEDIDO!\033[m')

