"""
Faça um programa que leia o ano de nascimento de um
jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que 
falta ou que passou do prazo.
"""
from datetime import date
ano_atual = date.today().year
# ano_atual = 2017 # Referencia ano do vídeo 
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_de_nascimento

if idade == 18:
    print(f'Você nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    tempo_para_alistar = 18 - idade
    ano_do_alistamento = tempo_para_alistar + ano_atual
    print(f'Você nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Ainda faltam {tempo_para_alistar} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_do_alistamento}')

elif idade > 18:
    tempo_para_alistar = idade - 18
    ano_do_alistamento = ano_atual - tempo_para_alistar
    print(f'Você nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Você já deveria ter se alistado há {tempo_para_alistar} anos.')
    print(f'Seu alistamento foi em {ano_do_alistamento}')
    

















