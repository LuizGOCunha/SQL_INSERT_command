from functions import *

print('Bem-vindo ao criador de personagem, edição Nergália.')
print('Insira abaixo a quantidade de Npcs que gostaria de criar.')
rep = input('>')

output = open('output.sql', 'w')
quantidade = 'n' * int(rep)
for n in quantidade:
    output.write(insert_rpg())

print('Output formado com sucesso')
print('Verifique o arquivo de output para obter seu mock data')


































