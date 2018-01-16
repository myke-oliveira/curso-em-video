#! /usr/bin/python3.6

print(
'''Faça um programa que mostre na tela
uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.'''
)

from time import sleep

for i in range(10, 0, -1):
    print(i, end = '', flush=True)
    sleep(1)
    print('\r    \r', end = '', flush=True)
print('Bummmm!!!')