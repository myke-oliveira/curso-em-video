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

print('Cada um dos dígitos: ')
print('{} - {} - {} - {}'.format(
    num //1000,
    (num // 100) % 10,
    (num // 10) % 10,
    num % 10
))