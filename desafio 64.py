#! /usr/bin/python3.6

print(
'''Crie um programa que leia \033[34mvários
números\033[m inteiros pelo teclado. O programa só
vai parar quando o usuário digitar o valor
\033[33m999\033[m, que é a condição de parada. No final,
mostre quantos números foram 
digitados e qual foi a soma entre eles.
\033[37m(desconsiderando o flag)\033[m.
'''
)

n = 1
soma = 0
qtd = 0
while n != 999:
    n = int(input('Número: '))
    soma += n
    qtd += 1
soma -= 999
qtd -= 1
print('Soma: {}'.format(soma))
print('Quantidade: {}'.format(qtd))