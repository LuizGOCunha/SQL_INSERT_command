import random


def insert_rpg():
    insert_statement = f"INSERT INTO nergalia (nome, profissao, nacionalidade, idade)"
    sex_value = random.randint(1,2)
    if sex_value == 1:
        nomes_masc = organizador('nomes_masc.txt')
        columnv1 = nomes_masc[random.randint(0,104)]
        profissoes_masc = organizador('profissoes_masc.txt')
        columnv2 = profissoes_masc[random.randint(0,25)]
    if sex_value == 2:
        nomes_fem = organizador('nomes_fem.txt')
        columnv1 = nomes_fem[random.randint(0,114)]
        profissoes_fem = organizador('profissoes_fem.txt')
        columnv2 = profissoes_fem[random.randint(0,13)]
    nacionalidade = ["NiKan", 'Proelia', 'Dannum', 'Zarbatus']
    columnv3 = nacionalidade[random.randint(0,3)]
    if columnv2 in ['abençoado', 'abençoada']:
        columnv4 = random.randint(50,800)
    else:
        columnv4 = random.randint(16,110)
    value_statement =f" VALUES ('{columnv1}', '{columnv2}', '{columnv3}', {columnv4});\n"
    return insert_statement + value_statement


def organizador(arquivo):
    nomes1 = open(f'{arquivo}', 'r')
    nomes2 = nomes1.read()
    lista = nomes2.split('\n')
    return lista
