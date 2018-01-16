#! /usr/bin/python3.6
from time import sleep
from random import randint

opcoes = ('PEDRA', 'PAPEL', 'TESOURA')

print(
'''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA'''
)
op_jog = int(input('Qual é a sua jogada? '))
if op_jog not in range(0, 3):
    print('Opção inválida.')
    exit(1)
op_com = randint(0, 2)
print('JO')
sleep(.35)
print('KEN')
sleep(.35)
print('PO!!!')
print('-='*10)
print('Computador jogou {}.'.format(opcoes[op_com]))
print('Jogador jogou {}.'.format((opcoes[op_jog])))
print('-='*10)
if (op_com, op_jog) == (0, 0) or (op_com, op_jog) == (1, 1) or (op_com, op_jog) == (2, 2):
    print('EMPATE.')
elif (op_com, op_jog) == (0, 2) or (op_com, op_jog) == (1, 0) or (op_com, op_jog) == (2, 1):
    print('Computador VENCE.')
else:
    print('Jogador VENCE.')