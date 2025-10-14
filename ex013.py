'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.
'''
salario_atual = float(input('Digite o valor do salário do funcionário: R$'))
salario_aumento = salario_atual + (salario_atual * (15 / 100))
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario_atual,salario_aumento))
