#! /usr/bin/python3.6

from math import ceil

print(
'''Crie um programa que leia uma frase
qualquer e diga se ela é um palindromo,
desconsiderando os espaços.
'''
)

print('Digite a frase:')
frase = input()
frase = frase.replace(' ','').upper()
é_palindromo = True
for i in range(ceil(len(frase)/2)):
    if frase[i] != frase[-1-i]:
        é_palindromo = False
print('É palindromo: {}'.format('Sim' if é_palindromo else 'Não'))