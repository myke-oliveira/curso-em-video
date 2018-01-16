#! /usr/bin/python3.6

print(
'''Faça um programa que leia o peso de
cinco pessoas. No final mostre qual foi o
maior e o menor peso lidos
'''
)
maior = float('-Infinity')
menor = float('+Infinity')
for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('Menor: {}'.format(menor))
print('Maior: {}'.format(maior))