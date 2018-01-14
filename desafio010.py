print('{:=^50}'.format('Desafio 10'))
print('Crie um programa que leia quanto dinheiro')
print('uma pessoa tem na carteira e mostre quantos')
print('dolares ela pode comprar.')
print('')
print('Considere')
print('US$ 1.00 = R$ 3.27')
print('{:=^50}'.format('Início'))
while True:
    try:
        tem = float(input('Quanto você tem? '))
        break
    except ValueError:
        print('Valor digitado inválido.')
print("Você pode comprar US$ {:.2f}.".format(tem / 3.27))
print('{:=^50}'.format('Fim'))