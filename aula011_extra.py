#! /usr/bin/python3.6

from itertools import product

styles = (0, 1, 4, 7)
texts = tuple(range(30,38))
backs = tuple(range(40, 48))

print('Styles =', styles)
print('Texts =', texts)
print('Backs =', backs)

for style, text, back in product(styles, texts, backs):
    print('\033[{};{};{}mTeste\033[m'.format(style, text, back))
