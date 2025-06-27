"""
Refaça o Desafio 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""

print('-=' * 20)
print('Analisador de Triângulo')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segment: '))

if r1 == r2 and r2 == r3 and r1 == r3:
    print('Com os segmentos digitados forma-se um triângulo: EQUILÁTERO!')
elif r1 != r2 and r2 != r3 and r1 != r3:
    print('Com os segmentos digitados forma-se um triângulo: ESCALENO!')
else:
    print('Com os segmentos digitados forma-se um triângulo: iSÓSCELES !')
    
