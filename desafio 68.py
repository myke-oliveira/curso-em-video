#! /usr/bin/python3.6

from random import randint

print(
'''Faça um programa que jogue par ou impar
com o computador. O jogo só será
interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
'''
)

vitorias = 0
while True:
    while True:
        us = input('Par ou impar? [P/I] ').upper()
        if us == 'P' or us == 'I':
            break
        print('Dados inválidos.')
    while True:
        try:
            n_us = int(input('Quantos dedos? '))
            if 1 <= n_us <= 10:
                break
        except ValueError:
            print('Dados inválidos.')
    co = 'P' if us == 'I' else 'I'
    n_co = randint(1, 10)
    total = n_co + n_us
    eh_par = total % 2 == 0
    print('*' * 22)
    print(f'Computador: {co}')
    print(f'Dedos do computador: {n_co}')
    if eh_par and us == 'P' or not eh_par and us == 'I':
        print('Você venceu!')
        print('Vamos jogar novamente!')
        print('-=' * 11)
        print()
        vitorias += 1
    else:
        print('Você perdeu!')
        print('Fim de jogo.')
        break
print()
print('-=' * 11)
print(f'Total de vitórias: {vitorias}')