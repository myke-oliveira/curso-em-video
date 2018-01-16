#! /usr/bin/python3.6

print(
'''Desenvolva um programa que leia seis
números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor
digitado for ímpar
desconsidere-o.'''
)

soma = 0
for i in range(1, 7):
    entrada = int(input('Número {}: '.format(i)))
    if entrada % 2 == 0:
        soma += entrada
print('Soma dos pares =', soma)