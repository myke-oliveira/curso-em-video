#! /usr/bin/python3.6

pnormal = float(input('Preço normal: R$ '))
print(
'''Condições de Pagamento:
[1] à vista (dinheiro/cheque) \033[34m10% de desconto\033[m
[2] à vista no cartão \033[34m5% de desconto\033[m
[3] em 2x no cartão
[4] em 3x ou mais no cartão \033[31m20% de juros\033[m'''
)
op = int(input('Sua opção: '))
if op == 1:
    p = pnormal * .9
    print('Será pago R$ {:.2f} à vista.'.format(p))
elif op == 2:
    p = pnormal * .95
    print('Será pago R$ {:.2f} à vista no cartão.'.format(p))
elif op == 3:
    p = pnormal
    print('Será pago R$ {:.2f} em 2x de R$ {:.2f} no cartão.'.format(p, p/2))
elif op == 4:
    nparcelas = int(input('Quantidade de parcelas: '))
    p = pnormal * 1.2
    print('Será pago R$ {:.2f} em 3x de R$ {:.2f} no cartão.'.format(p, p/nparcelas))
else:
    print('Opção inválida')
