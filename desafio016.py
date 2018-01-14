print('{:*^50}'.format('Desafio 16'))
print('  Crie um programa que leia um número Real')
print('qualquer pelo teclado e mostre na tela a sua por-')
print('ção inteira.')
print('{:*^50}'.format('Início'))
while True:
    try:
        num = float(input('Digite o número Real: '))
        break
    except:
        print('Valor inválido.')

import math

print('O valor da parte inteira de {} é: {}'.format(num, math.floor(num)))

print('{:*^50}'.format('Fim'))