print('{:=^50}'.format('Desafio 09'))
print('Faça um programa que leia um número')
print('inteiro qualquer e mostre na tela a sua')
print('tabuada.')
print('{:=^50}'.format('Início'))
while True:
    try:
        n = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Valor inválido.')
for i in range(1, 10):
    print('{} x {} = {:>5}'.format(n, i, n*i))
print('{:=^50}'.format('Fim'))