'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento.
'''
salario_atual = float(input('Digite o valor do salário do funcionário: R$'))
salario_aumento = salario_atual + (salario_atual * (15 / 100))
print('O novo salário do funcionário com aumento de 15% vai passar a ser R${}'.format(salario_aumento))
