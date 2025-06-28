"""
Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
print('\033[33m=-=\033[m' * 20)
print(f'\033[35m{"Cálculo IMC":^55}\033[m')
print('\033[33m=-=\033[m' * 20)

peso = float(input('Digite seu peso (ex.: 100.0): '))
altura = float(input('Digite sua altura (ex.: 1.70): '))

imc = peso / (altura * altura)

if imc <= 18.5:
    print('Você está abaixo do peso.')
    print(f'\033[33mSeu IMC: {imc:.2f}\033[m')
elif imc <= 25: 
    print('Você está com o peso ideal. Parabéns!')
    print(f'\033[32mSeu IMC: {imc:.2f}\033[m')
elif imc <= 30:
    print('Você está com Sobrepeso.')
    print(f'\033[34mSeu IMC: {imc:.2f}\033[m')
elif imc <= 40:
    print('Você está com Obesidade.')
    print(f'\033[34mSeu IMC: {imc:.2f}\033[m')
else:
    print('Você está com Obesidade mórbida.')
    print(f'\033[34mSeu IMC: {imc:.2f}\033[m')
