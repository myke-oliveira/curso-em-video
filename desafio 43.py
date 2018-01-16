#! /usr/bin/python3.6

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / altura / altura
print('IMC: {:.1f}'.format(imc))
res = 'ABAIXO DO PESO' if imc <= 18.5 else 'PESO NORMAL' if imc <= 24.9 else 'SOBREPESO' if imc <= 29.9 else 'OBESIDADE GRAU I' if imc < 34.9 else 'OBESIDADE GRAU II' if imc < 39.9 else 'OBESIDADE GRAU III'
print('Você está {}.'.format(res))