# Desenvolva um programa que leia as duas notas de um aluno,
# e mostre sua média.

nota1 = float(input('Informe a primeiro nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

print('A média do aluno é: {:.2f}'.format(media))
