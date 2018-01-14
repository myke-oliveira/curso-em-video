print('{:*^50}'.format('Desafio 18'))
print('Faça um programa que leia um ângulo qualquer e mos-')
print('tre na tela o valor do seno, cossenoe tangênge desse')
print('ângulo.')
print('{:*^50}'.format('Início'))
import math
while True:
    try:
        deg = float(input('Digite o valor do ângulo: '))
        break;
    except ValueError:
        print('Valor digitado inválido. Por favor digite um valor válido.')
rad = deg / 180 * math.pi
print('Seno: {}'.format(math.sin(rad)))
print('Cossenoo: {}'.format(math.cos(rad)))
print('Tangente: {}'.format(math.tan(rad)))


print('{:*^50}'.format('Fim'))