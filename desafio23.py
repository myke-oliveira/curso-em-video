''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''
while True:
    try:
        num = int(input('Digite um número de 0 a 9999: '))
        if 0 < num and num < 9999:
            break
        else:
            raise ValueError
    except ValueError:
        print(' Valor inválido!')

s = '{:0>4}'.format(num)
print('Cada um dos dígitos: ')
print('{} - {} - {} - {}'.format(
    s[0],
    s[1],
    s[2],
    s[3]
))