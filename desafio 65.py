#! /usr/bin/python3.6

from math import inf

print(
'''Crie um programa que leia vários
números inteiros pelo teclado. No final da
execução, mostre a média entre todos os
valores e qual foi o maior e o menor
valores lidos. O programa deve
perguntar ao usuário se ele quer ou não
continuar a digitar valores.
'''
)

continuar, media, n = True, 0, 0
maior, menor = -inf, inf
while continuar:
    x = int(input('Valor inteiro: '))
    media += x
    n += 1
    maior = x if x > maior else maior
    menor = x if x < menor else menor
    continuar = input('Deseja continuar? [S/N] ').upper() == 'S'
media /= n
print('Média: {}'.format(media))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
