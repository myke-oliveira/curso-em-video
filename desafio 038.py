#! /usr/bin/python3.6

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
if n1 < n2:
    print('O \033[1;32mSEGUNDO\033[m número é \033[1;31mMAIOR\033[m.')
elif n1 > n2:
    print('O \033[1;32mPRIMEIRO\033[m número é \033[1;31mMAIOR\033[m.')
else:
    print('Os números são \033[1;31mIGUAIS\033[m.')