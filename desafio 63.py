#! /usr/bin/python3.6

print(
'''Escreva um programa que leia um
número n inteiro qualquer e mostre na
tela os n primeiros elementos de uma
Sequência de Fibonacci.
'''
)

n = int(input('n: '))
fi = 0
fi1 = 1
for i in range(n):
    print(fi, '-', end = ' ')
    fi, fi1 = fi1, fi + fi1
print('\b\b\b')