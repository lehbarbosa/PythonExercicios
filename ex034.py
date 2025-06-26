# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Informe o salário do funcionário? R$'))

aumento_10_porc = salario * (10 / 100) + salario

aumento_15_porc = salario * (15 / 100) + salario

if salario > 1250:
    print(f'Quem recebe {salario:.2f} vai passar receber {aumento_10_porc:.2f}')
else:
    print(f'Quem recebe {salario:.2f} vai passar receber {aumento_15_porc:.2f}')
