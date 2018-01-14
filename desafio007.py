print('{:=^50}'.format('Desafio 07'))
print('Desenvolva um programa que leia as duas')
print('notas de um aluno, calule e mostre a sua')
print('média.')
print('{:=^50}'.format('Início'))
while True:
    try:
        n1 = float(input('Digite a 1ª nota: '))
        break
    except ValueError:
        print('Valor inválido.');

while True:
    try:
        n2 = float(input('Digite a 2ª nota: '))
        break
    except:
        print('Valor inválido.');
print('A média do aluno foi: {:.2f}'.format((n1 + n2)/2))
print('{:=^50}'.format('Fim'))