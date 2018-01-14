print('{:*^50}'.format('Desafio 20'))
print('  O mesmo professor do desafio anterior quer sor-')
print('tear a ordem de apresentação de trabalhos dos alu-')
print('nos. Faça um programa que leia o nome dos quatro')
print('alunos e mostre a ordem sorteada.')
print('{:*^50}'.format('Início'))
alunos = []
for i in range(1, 5):
    alunos.append(input('Digite o nome do aluno {}: '.format(i)))
import random
random.shuffle(alunos)
# print(alunos)
for i in range(4):
    print('Aluno {}: {}'.format(i + 1 , alunos[i]))

print('{:*^50}'.format('Fim'))