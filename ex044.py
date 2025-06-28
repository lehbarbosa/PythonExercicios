"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:

_ À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
print('\033[33m=-=\033[m' * 20)
print(f'\33[1;35m{"Mercado Bom Preço":^50}\033[m')
print('\033[33m=-=\033[m' * 20)

produto = float(input('Qual o valor do produto: R$'))
print("""\033[36mEscolha a forma de pagamento:
[ 1 ] Á vista dinheiro/cheque: 10% de desconto
[ 2 ] À vista no cartão: 5% de desconto
[ 3 ] Em até 2x no cartão: preço normal       
[ 4 ] 3x ou mais no cartão: 20% de juros\033[m""")
opcao = int(input('Digite a opção: '))

if opcao == 1:
    apagar = produto - (produto * (10 / 100))
    print(f'O total a pagar com desconto é R${apagar}')
elif opcao == 2:
    apagar = produto - (produto * (5 / 100))
    print(f'O total a pagar com desconto é R${apagar}')
elif opcao == 3:
    print(f'O total a pagar é {produto}')
elif opcao == 4:
    apagar = produto + (produto * (20 / 100))
    print(f'O total apagar com juros R${apagar}')
else:
    print('Opção inválida. Por favor, escolha apenas as opçoes do menu.')