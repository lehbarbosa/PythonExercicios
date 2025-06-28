"""
A Confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master
"""
# from datetime import date
ano_de_nascimeto = int(input('Informe o ano de nascimento do atleta: '))
# ano_atual = date.today().year
ano_atual = 2017 # Ano do video do curso
idade = ano_atual - ano_de_nascimeto
print(f'O atleta tem idade de {idade} anos.')

if idade <= 9:
    print('A categoria do atleta é: Mirim')
elif idade <= 14:
    print('A categoria do atleta é: Infantil')
elif idade <= 19:
    print('A categoria do atleta é: Junior')
elif idade <= 25:
    print('A categoria do atleta é: Sênior')
elif idade > 25:
    print('A categoria do atleta é: Master')

