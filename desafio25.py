''' Crie um programa que verifique se o nome possui "Silva".'''
nome = input('Digite o nome: ').strip()
print('O nome possui "Silva": {}'.format('silva' in nome.lower()))