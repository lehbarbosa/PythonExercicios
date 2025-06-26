# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagem até 200km
# e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distância percorrida na viagem (km): '))
print(f'Você está preste a começar uma viagem de {distancia:.2f}km.')

if distancia <= 200:
    preco_viagem = distancia * 0.50
    print(f'Sua passagem vai custar R${preco_viagem:.2f}')
else:
    preco_viagem = distancia * 0.45
    print(f'Sua passagem vai custar R${preco_viagem:.2f}')

print('Tenha uma boa viagem!')
