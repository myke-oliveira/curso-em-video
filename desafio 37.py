#! /usr/bin/python3.6

num = int(input('Digite um número inteiro: '))
print(
'''
Escolha uma das bases para conversão:
    [1] converter para BINÁRIO.
    [2] converter para OCTAL
    [3] converter para HEXADECIMAL'''
)
op = int(input('Sua Opção: '))
if op == 1:
    conv_type = 'BINÁRIO'
    conv = bin(num)[2:]
elif op == 2:
    conv_type = 'OCTAL'
    conv = oct(num)[2:]
elif op == 3:
    conv_type = 'HEXADECIMAL'
    conv = hex(num)[2:]
else:
    print('Opção inválida')
    exit(1)
print('{} convertido para {} é igual a {}.'.format(num, conv_type, conv))