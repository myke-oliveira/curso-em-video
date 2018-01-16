#! /usr/bin/python3.6

import os

print(
'''Crie um programa que leia dois valores e
mostre um menu na tela.

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

Seu programa deverá realizar a operação
solicitada em cada caso.
'''
)
op = 4
while op != 5:
    if op == 4:
        v1 = float(input('Valor 1: '))
        v2 = float(input('Valor 2: '))
    print(
    '''Menu
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    '''
    )
    op = int(input('Sua opção: '))
    if op == 1:
        print('{} + {} = {}'.format(v1, v2, v1 + v2))
    elif op == 2:
        print('{} * {} = {}'.format(v1, v2, v1 * v2))
    elif op == 3:
        print('Maior: {}'.format(v1 if v1 > v2 else v2))
    if op != 4:
        input()
    os.system('clear')
