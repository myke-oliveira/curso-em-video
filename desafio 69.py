#! /usr/bin/python3.6

print(
'''Crie um programa que leia a idade e o
sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar.
No final mostre

a) quantas pessoas tem mais de 18 anos.
b) quantos homens foram cadastrados.
c) quantas mulheres tem menos de 20 anos.

'''
)

i = 1
pessoas_com_mais_de_18 = homens = mulheres_com_menos_de_20 = 0
while True:
    print(f'Cadastrando pessoa {i}')
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Dados inválidos, digite novamente.')
    while True:
        sexo = input('Sexo: [M/F] ').upper()
        if sexo == 'M' or sexo == 'F':
            break
        print('Dados inválidos, digite novamente.')
    if idade > 18:
        pessoas_com_mais_de_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_com_menos_de_20 += 1
    while True:
        op = input('Deseja cadastrar mais uma pessoa? [S/N] ').upper()
        print()
        if op == 'S' or op == 'N':
            break
    if op == 'N':
        break
    i += 1
print(f'Maiores de 18: {pessoas_com_mais_de_18}')
print(f'Homens: {homens}')
print(f'Mulheres com menos de 20 anos: {mulheres_com_menos_de_20}')

