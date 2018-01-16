#! /usr/bin/python3.6

s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        print('Os segmentos acima formam um \033[34mTRIÂNGULO EQUILÁTERO\033[m.')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('Os segmentos acima formam um \033[34mTRIÂNGULO ISÓCELES\033[m.')
    else:
        print('Os segmentos acima formam um \033[34mTRIÂNGULO ESCALENO\033[m.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR UM TRIÂNGULO\033[m.')