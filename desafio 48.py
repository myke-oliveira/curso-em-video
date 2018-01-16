#! /usr/bin/python3.6

print(
'''Faça um programa que calcule e soma
entre todos os números ímpares que
são múltiplos de três e que se encontram
no interfalo de 1 até 500.'''
)

soma = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        soma += i
print('Soma =', soma)