largura = float(input('Informe a largura da parede: '))
comprimento = float(input('Informe o comprimento da parede: '))
area = largura * comprimento
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m².'.format(largura, comprimento, area))
litros = area / 2
print('Para pintar essa parede, você vai precisar de {}l de tinta.'.format(litros))


