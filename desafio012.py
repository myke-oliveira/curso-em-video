print('{:=^50}'.format('Desafio 12'))
print('Faça um algoritmo que leia o preço de um produto')
print('e mostre seu novo preço com 5% de desconto.')
print('{:=^50}'.format('Início'))
while True:
    try:
        preco = float(input('Digite o preço de um produto: '))
        break
    except ValueError:
        print('Valor inválido.')
print('O preço do produto com desconto de 5 % é: {:.2f}'.format(preco * .95))
print('{:=^50}'.format('Fim'))
