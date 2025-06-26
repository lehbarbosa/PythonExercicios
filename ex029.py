# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
velocidade_carro = float(input('Digite a velocidade do carro em km/h: '))

if velocidade_carro > 80:
    print('Você foi multado! Excedeu o limite de velocidade de 80km/h')
    multa = (velocidade_carro - 80) * 7
    print(f'O valor da sua multa vai custar R${multa:.2f}')
else:
    print('PARABÉNS, você está andando dentro do limite de velocidade, continue assim.')
    print('Tenha um bom dia, dirija com segurança.')
