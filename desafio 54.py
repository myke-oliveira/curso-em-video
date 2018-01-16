#! /usr/bin/python3.6

print(
'''Crie um programa que leia o nao de
nascimento de sete pessoas. No final
mostre quantas pessoas ainda não
atingiram a maioridade e quantas já
são maiores'''
)

maiores = 0
for i in range(1, 8):
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    if idade >= 21:
        maiores +=1
print('Há {} pessoas que atingiram a maioridade.'.format(maiores))