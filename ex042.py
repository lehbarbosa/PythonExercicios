"""
Refaça o Desafio 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo
será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
print('-=' * 20)
print(f'{"Analisador de Triângulo":^40}')
print('-=' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceito segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo!', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 and r1 != r3:
        print('ESCALENO.')
    else:
        print('ISÓCELES.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')



