'''
Exercício Python 57: 
Faça um programa que leia o sexo de uma pessoa, mas só
aceite os valores 'M' e 'F'.
Caso esteja errado, peça a digitação novamente  até ter um
valor correto.
'''
sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    print('Entrada inválida!')
    sexo = str(input('Digite novamente o sexo da pessoa: ')).strip().upper()[0]
    print('-' * 15)
print('Sexo {} registrado com sucesso!'.format(sexo))

