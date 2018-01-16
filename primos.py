#! /usr/bin/python3.6

from time import sleep

def eh_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primos():
    n = 2
    while True:
        if eh_primo(n):
            yield n
        n += 1

def fatores(n):
    ret = []
    for fator in primos():
        expoente = 0
        while n % fator == 0:
            n /= fator
            expoente += 1
        if expoente != 0:
            ret.append((fator, expoente))
        if n == 1:
            break
    return ret

def mostrar_primos():
    for i in primos():
        print(i)
        sleep(.5)

def fatorar_numeros(n):
    for i in range(1, n+1):
        print(f'Fatores de {i}: {fatores(i)}.')

fatorar_numeros(100)
