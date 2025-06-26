# Faça um programa que leia um ano qualquer e mostre
# se ele é BISSEXTO.
# ano = int(input('Digite um ano para verificar se é Bissexto: '))

# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano  % 400 == 0:
#             print(f'{ano} é um ano Bissexto!' )
#         else:
#             print(f'{ano} não é um ano Bissexto!')    
#     else:
#         print(f'{ano} é um ano Bissexto!')
# else:
#     print(f'{ano} não é um ano Bissexto!')

# Resolução Prof.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))
