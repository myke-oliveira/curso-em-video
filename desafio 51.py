#! /usr/bin/python3.6

print(
'''Desenvolva um programa que leia o
primeiro termo e a razão de uma PA. No
final, mostre os 10 primeiros termos
dessa progressão.'''
)

a = float(input('Primeiro termo: '))
r = float(input('Razão: '))
print('(', end='')
for i in range(1, 11):
    print(a, end= ', ')
    a += r
print('\b\b)')