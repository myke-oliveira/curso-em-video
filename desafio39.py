#! /usr/bin/python3.6

from datetime import datetime

ano_nascimento = int(input('Ano de nascimento: '))
ano = datetime.now().year
idade = ano - ano_nascimento
ano_alistamento = ano_nascimento + 18
print('Quem nasceu em {} tem {} anos em {}.'.format(ano_nascimento, idade, ano))
if ano_alistamento < ano:
    print('Você ja deveria ter se alistado há {} anos'.format(ano - ano_alistamento))
    print('O seu alistamento foi em {}.'.format(ano_alistamento))
elif ano_alistamento == ano:
    print('Você deve se alistar esse ano.')
    print('O seu alistamento é em {}.'.format(ano_alistamento))
else:
    print('Você deverá se alistar daqui a {} anos'.format(ano_alistamento - ano))
    print('O seu alistamento será em {}.'.format(ano_alistamento))