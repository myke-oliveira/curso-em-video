
from datetime import datetime

nasc = int(input('Ano de nascimento: '))
ano = datetime.now().year
idade = ano - nasc
print('Idade: {}'.format(idade))
categoria = 'MIRIM' if idade <= 9 else 'INFANTIL' if idade < 14 else\
    'JUNIOR' if idade <= 19 else 'SENIOR' if idade <= 25 else 'MASTER'
print('Categoria: {}'.format(categoria))