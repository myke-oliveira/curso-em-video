print('{:=^50}'.format('Desafio 13'))
print('Faça um algortimo que leia o salário de um')
print('funcionário e mostre seu novo salário com ')
print('15% de aumento.')
print('{:=^50}'.format('Início'))
while True:
    try:
        s = float(input('Digite o salário do funcionário: '))
        break
    except ValueError:
        print('Valor digitado inválido.')
print('O novo salário do funcionário com 15% de aumento é: {}'.format(s*1.15))
print(f'{"Fim":=^50}')