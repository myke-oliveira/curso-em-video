print('{:=^50}'.format('Desafio 6'))
print('Crie um algoritmo que leia um número e mostre o')
print('seu dobro, triplo e raiz quadrada.')
print('{:=^50}'.format('Inicio'))
n = input('Digite um número: ')
if n.isnumeric():
    n = int(n)
    print('Dobro: {:.>23}'.format(2*n))
    print('Triplo: {:.>22}'.format(3*n))
    print('Raiz Quadrada: {:.>15}'.format(n**(1/2)))
else:
    print('Valor digitado não numérico.')
print('{:=^50}'.format('Fim'))