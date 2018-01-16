#! /usr/bin/python3.6

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('Média: {:.2}'.format(média))
if média < 5:
    print('O aluno está \033[31mREPROVADO\033[m.')
elif média < 7:
    print('O aluno está em \033[32mRECUPERAÇÃO\033[m.')
else:
    print('O alno está \033[34mAPROVADO\033[m.')