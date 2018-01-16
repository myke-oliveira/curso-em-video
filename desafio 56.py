#! /usr/bin/python3.6

soma = 0
maior_idade_homem = float('-Infinity')
mulheres_com_menos_de_20_anos = 0
for i in range(1, 5):
    print('Entre com os dados da {}ª pessoa.'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (m/f): ')
    soma += idade
    if idade > maior_idade_homem and sexo == 'm':
        maior_idade_homem = idade
        homem_mais_velho = nome
    if idade < 20 and sexo == 'f':
        mulheres_com_menos_de_20_anos += 1
    print()
média = soma/4
print('Média de idade: {:.2f}'.format(média))
print('Homem mais velho: {}'.format(homem_mais_velho))
print('Quantas mulheres com menos de 20 anos: {}'.format(mulheres_com_menos_de_20_anos))