print('{:*^50}'.format('Desafio 14'))
print('Escreva um programa que converta uma tem-')
print('peratura digitada em ºC e converta para')
print('ºF.')
print('{:*^50}'.format('Início'))
while True:
    try:
        C = float(input('Digite a temperatura em graus Celsius: '))
        break
    except ValueError:
        print('Valor digitado inváido.')
F = C * 1.8 + 32
print('O valor da temperatura de {}ºC é: {}ºF.'.format(C, F))

print('{:*^50}'.format('Fim'))