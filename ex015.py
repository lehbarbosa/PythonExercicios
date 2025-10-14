'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
'''
distancia = float(input("Informe a distância percorrida [km]: "))
dia = int(input("Informe quantos dias você utilizo o carro: "))
custo_dia = dia * 60
total = distancia * 0.15 + custo_dia
print("Você utlizou o carro por {} dias, e percorreu {}Km".format(dia, distancia))
print("O total a pagar é de R${:.2f}".format(total))
