print('{:=^50}'.format('Desafio 05'))
print('    Faça um programa que leia um número inteiro e')
print('mostre na tela o seu antecessor e o seu sucessor.')
print('{:=^50}'.format('Início'))
n = input('Digite um número: ')
if n.isnumeric():
    n = int(n)
    print('Sucessor: {:10}'.format(n + 1))
    print('Antecessor: {:8}'.format(n - 1))
else:
    print('Valor digitado inválido.')
print('{:=^50}'.format('Fim'))
