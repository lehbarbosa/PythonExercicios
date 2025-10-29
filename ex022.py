"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas;
> O nome com todas minúsculas;
> Quantas letras ao todo (sem considerar espaços);
> Quantas letras tem o primeiro nome.
"""
nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome com letras maiúsculas é: {}".format(nome.upper()))
print("Seu nome com letras minusculas é: {}".format(nome.lower()))
print("Seu nome tem {} letras ao todo.".format(len(nome.replace(' ',''))))
print("Seu primeiro nome é {} tem {} letras".format(nome.split()[0], len(nome.split()[0])))
