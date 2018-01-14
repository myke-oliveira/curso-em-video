print('{:=^50}'.format('Desafio 08'))
print('Escreva um programa que leio um valor em ')
print('metros e exiba convertido em centímetros e')
print('milímetros.')
print('{:=^50}'.format('Início'))
while True:
    try:
        m = float(input('Digite o valor em metros: '))
        break
    except ValueError:
        print('Valor inválido')
print('O valor equivale a: ')
print('Centímetros: {:.>20} cm'.format(m*100))
print('Milímetros: {:.>21} mm'.format(m*1000))