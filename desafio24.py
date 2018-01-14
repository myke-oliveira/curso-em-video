''' crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra santo'''
cidade = input('Digite o nome da cidade: ').strip()
print('A cidade começa com a palavra Santo: {}'.format('Sim' if cidade.find('Santo') == 0 else 'Não'))