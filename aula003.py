#! /usr/bin/python3.6

n1 = int(input('\033[mDigite um número: \033[1;35m'))
n2 = int(input('\033[mDigite outro número: \033[1;35m'))
s = n1 + n2
print('\033[mA soma entre \033[1;35m{}\033[0;0m e \033[1;35m{}\033[0;0m vale \033[1;35m{}\033[0;0m.'.format(n1, n2, s))
