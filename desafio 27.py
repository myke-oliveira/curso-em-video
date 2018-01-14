''' Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o úmtimo nome separadamente.'''
print('Digite o seu nome Completo: ')
# A falta desse strip() não prejudica a execução.
nomes = input().strip().split()
print('Primeiro nome: {}'.format(nomes[0]))
print('Último nome: {}'. format(nomes[-1]))
