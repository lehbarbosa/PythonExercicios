# Faça um programa que leia uma frase pelo teclado e mostre:
# >Quantas vezes aparece a letra "A"
# >Em que posição ela aparece a primeira vez
# >Em que posição ela aparece a última vez

palavra = str(input('Digite uma frase: ')).lower().strip()

letra_a = palavra.count('a')
primeira_vez = palavra.find('a')    
segunda_vez = palavra.rfind('a') 

print('\nA letra "A ou a" aparece {} vezes  na frase'.format(letra_a))
print('A primeira vez que a letra "A ou a" aparece é {} posição'.format((primeira_vez) + 1))
print('A última vez que a letra "A ou a" aparece é {} posição'.format((segunda_vez) + 1))
