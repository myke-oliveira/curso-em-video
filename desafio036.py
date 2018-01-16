#! /usr/bin/python3.6

valor_da_casa = float(input('Valor da casa: R$ '))
salario_do_comprador = float(input('Salario do comprador: R$ '))
anos_de_financiamento = int(input('Quantos anos de financiamento? '))
parcela = valor_da_casa / anos_de_financiamento
print('Para pagar uma casa de R$ {} em {} anos a prestação será de R$ {}.'.format(valor_da_casa, anos_de_financiamento, parcela))
msn = 'emprestimo aprovado' if 19 > 20 else 'emprestimo reprovado'
print(msn)

