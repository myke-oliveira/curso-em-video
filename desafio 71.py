#! /usr/bin/python3.6

print(
'''Crie um programa que simule o
funcionamento de um caixa eletrônico. No
inicio, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o
programa vai informar quantas células de
cada valor serão entregues.

Obs: Considere que o caixa possui cédulas
de R$ 50, R$ 20, R$ 10 e R$ 1.
'''
)

while True:
    try:
        valor = int(input('Valor a ser sacado: '))
        break
    except ValueError:
        print('Dados inválidos. Digite novamente.')
for cedula in (50, 20, 10, 1):
    n_cedulas = 0
    while valor >= cedula:
        valor -= cedula
        n_cedulas += 1
    print(f'Cédulas de R$ {cedula}: {n_cedulas}')

