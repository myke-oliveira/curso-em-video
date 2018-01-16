#! /usr/bin/pyhton3.6

print(
'''
Faça um programa que leia um número
inteiro e diga se ele é ou não um 
número primo.
'''
)

num = int(input('Número: '))
eh_primo = True
for i in range(2,num):
    if num % i == 0:
        eh_primo = False
print('É primo: ', 'Sim' if eh_primo else 'Não')