#! /usr/bin/python3.6

print(
'''Melhore o jogo do DESAFIO 028 onde o
computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai
tentar advinhar até acertar, mostrando no
final quantos palpites foram necessários
para vencer.
'''
)

from random import randint

computador = randint(1, 10)
print('Estou pensando em um número, você consegue adivinhar qual é?')
usuário = 11
n_palpites = 0
while usuário != computador:
    usuário = int(input('Seu Palpite: '))
    n_palpites += 1
    if usuário != computador:
        print('Você errou.')
print('Parabéns, você acertou com {} palpites.'.format(n_palpites))