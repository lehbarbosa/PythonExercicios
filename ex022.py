# Crie um programa que leia o nome completo de uma pessoa e mostre: 
#   > O nome com todas as letras maiúsculas;
#   > O nome com todas minúsculas;
#   > Quantas letras ao todo (sem considerar espaços);
#   > Quantas letras tem o primeiro nome.

nome = str(input('Digite o nome de uma pessos: '))

print('O nome com todas as letras Maiúsculas fica:  {}'.format(nome.upper()))
print('O nome com todas as letras Minúsculas fica: {}'.format(nome.lower()))
print('Total de letras {} letras'.format(len(nome.replace(' ', ''))))

priNome = nome.split()
print('Quantas letras tem o primeiro nome {}: {} letras'.format(priNome[0], len(priNome[0])))
