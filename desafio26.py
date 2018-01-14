''' Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A"
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.'''

frase = input('Frase: ').strip()
MAIUSCULA = frase.upper()
print('Quantas vezes aparece a letra A: {}'.format(MAIUSCULA.count('A')))
print('Aparece na primeira vez: {}'.format(MAIUSCULA.find('A') + 1))
print('Aparece na última vez: {}'.format(len(MAIUSCULA) - MAIUSCULA[::-1].find('A')))
# Método Guanabara
# MAIUSCULA.rfind('A') + 1