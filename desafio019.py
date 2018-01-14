print('{:=^50}'.format('Desafio 19'))
print('  Um professor que sortear um dos seus quatro alu-')
print('nos para apagar o quadro. Faça um programa que a-')
print('jude ele, lendo o nome deles e escrevendo o nome')
print('do escolhido.')
print('{:=^50}'.format('Início'))
alunos = []
for i in range(1, 5):
    alunos.append(input('Digite o nome do aluno {}: '.format(i)))

from random import choice

print('O aluno escolhido é {}.'.format(choice(alunos)))

print('{:=^50}'.format('Fim'))