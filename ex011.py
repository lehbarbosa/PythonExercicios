# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta nescessária
# para pintá-la, sabendo que cada litro de tinta, pinta uma 
# área de 2m2.


largura = float(input('Informe a largura da parede: '))
comprimento = float(input('Informe o comprimento da parede: '))
area = largura * comprimento
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, comprimento, area))
litros = area / 2
print('Para pintar essa parede, você vai precisar de {}l de tinta.'.format(litros))


