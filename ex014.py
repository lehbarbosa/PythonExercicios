'''
 Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
'''
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print("A temperatura {}°C equivale {}°F".format(celsius, fahrenheit))
