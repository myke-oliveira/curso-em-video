print('{:*^50}'.format('Desafio 17'))
print('  Faça um programa que leia o comprimento do cate-')
print('to de um triângulo retângulo, calcue e mostre o')
print('comprimento da hipotenusa.')
print('{:*^50}'.format('Início'))
import enter
print('Entre com os Dados.')
C1 = enter.enter(float, 'Digite o cateto adjacente: ')
C2 = enter.enter(float, 'Digite o cateto oposto: ')
H = (C1**2 + C2**2)**0.5
print('O valor da hipotenusa é: {}'.format(H))
print('{:*^50}')