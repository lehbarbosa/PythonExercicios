"""
Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas.
> O nome com todas minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""

nome = input('Digite seu nome completo: ')
nome_sem_espaços = nome.replace(' ', '')
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras sem considerar espaços.'.format(len(nome_sem_espaços)))
nome_separado = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(nome_separado[0])))
