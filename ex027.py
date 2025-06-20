# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o segundo nome separadamente.
# >Ex.: 
# "Ana Maria de Souza"
# >primeiro: Ana
# >último: Souza

nome = str(input('Digite o nome completo: ')).split()

print('Prazer em te conhcer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu segundo nome é {}'.format(nome[-1]))
