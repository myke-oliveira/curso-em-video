print('{:*^50}'.format('Desafio 15'))
print('  Escreva um programa que pergunte a quantidade')
print('de Km percorridos por um carro aluugado e a')
print('quantidade de dias pelos quais ele foi')
print('alugado. Calcule o preço a pagar, sabendo que o ')
print('carro custa R$60 por dia e R$0,15 por Km rodado.')
print('{:*^50}'.format('Início'))
while True:
    try:
        Km = float(input('Digite o total de Km rodados: '))
        break
    except ValueError:
        print('Valor digitado inválido.')
while True:
    try:
        Dias = int(input('Digite a quantidade de dias pelos quais ele foi alugado: '))
        break
    except ValueError:
        print('Valor digitado inválido')
valor = 60 * Dias + 0.15 * Km
print('Total a pagar: {}'.format(valor))
print('{:*^50}'.format('Fim'))
