# Faça um algoritmo que leia  o salário  de um funcionário 
# e mostre  seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário do funcionário: R$'))
novoSalario = salario + (salario * (15 / 100))
print('O novo salário vai passar a ser de R${:.2f}.'.format(novoSalario))
