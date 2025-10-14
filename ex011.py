'''
Faça um pograma que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
'''
altura = float(input('Dgite a largura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print("Sua parede tem dimensão de {}x{} e sua área é de {}m².".format(altura, largura, area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}l de tinta'.format(tinta))
