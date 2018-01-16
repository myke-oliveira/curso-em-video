#! /usr/bin/python3.6

print(
'''Faça um programa que leia um número
qualquer e mostre o seu fatorial.'''
)

x = int(input('Número: '))
fatorial = 1
while x > 1:
    fatorial *= x
    x -= 1
print('Fatorial: {}'.format(fatorial))