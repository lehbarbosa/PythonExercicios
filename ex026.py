# Faça um programa que leia uma frase pelo teclado e mostre:
# >Qauntas vezes aparece a letra "A"
# >Em que posição ela aparece a primeira vez
# >Em que posição ela aparece a última vez

palavra = str(input('Digite uma frase: ')).lower()

letra_a = palavra.count('a')
primeira_vez = palavra.find('a')    
segunda_vez = palavra.rfind('a') 

print('\nA letra "A ou a" aparece {} vezes  na frase'.format(letra_a))
print('\nA primeira vez que a letra "A ou a" aparece é {}º posição'.format(primeira_vez))
print('\nA última vez que a letra "A ou a" aparece é {}º posição'.format(segunda_vez)) 
