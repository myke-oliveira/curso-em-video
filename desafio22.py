''' Crie um programa que leia o nome completo de uma pessoa e mostre:

O nome com todas as letras maiúsculas.
O nome con todas minusculas.
Quantas letras ao todo (sem  considerar espaços).
Quantas letras tem o primeiro nome.'''

print('Digite o nome completo da pessoa: ')
nome = input().strip()
print()
print('O nome com todas as letras maiúsculas:')
print(nome.upper())
print()
print('O nome com todas as letras minúsculas: ')
print(nome.lower())
print()
print('Quantas letras ao todo (sem considerar os pespaços): {}'.format(len(nome.replace(' ', ''))))
# len(nome) - nome.count(' ')
print()
print('Quantas letras tem o primeiro nome: {}'.format(len(nome.split()[0])))
# Método Guanabara
# nome.find(' ')