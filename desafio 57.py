#! /usr/bin/python3.6

print(
'''Faça um programa que leia o sexo de uma
pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação
novamente até ter um valor correto.'''
)

sexo = input('Digite o seu sexo: [M/F] ').upper()
while(sexo != 'M' and sexo != 'F'):
    sexo = input('Dados incorretos, digite novamente: [M/F] ').upper()
print('Sexo: {}'.format(sexo))
