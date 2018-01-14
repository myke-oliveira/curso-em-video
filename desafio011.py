from builtins import ValueError

print('{:=^50}'.format('Desafio 11'))
print('Faça um programa que leia a largura e a altura de uma ')
print('parede em metros, calcule a sua área e a quantidade de')
print('tinta necessária para pinta-la sabendo que cada litro de')
print('tinta pinta uma área de 2 m²')
print('{:=^50}'.format('Início'))
while True:
    try:
        l = float(input('Digite a largura da parede: '))
        break
    except ValueError:
        print('Valor inválido')
while True:
    try:
        h = float(input('Digite a altura da parede: '))
        break
    except ValueError:
        print('Valor inválido')
a = l * h
print('A área da parede: {}'.format(a))
q = a / 2
print('Quantidade de tinta para pinta-la: {}'.format(q))
print('{:=^50}'.format('Fim'))
