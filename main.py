print('Nome da tabela')
table = input(">")
print('Nome das colunas a serem utilizadas, separadas por virgula e espaço.')
column_string = input(">")
column_list = column_string.split(", ")
if len(column_list) == 2:
    column1, column2 = column_list
elif len(column_list) == 3:
    column1, column2, column3 = column_list
elif len(column_list) == 4:
    column1, column2, column3, column4 = column_list
print('Valores das colunas, separadas por virgula e espaço.')
value_string = input(">")
value_list = value_string.split(", ")
if len(value_list) == 2:
    columnv1, columnv2 = value_list
elif len(value_list) == 3:
    columnv1, columnv2, columnv3 = value_list
elif len(value_list) == 4:
    columnv1, columnv2, columnv3, columnv4 = value_list


def insert(table, column1, columnv1, column2, columnv2, column3=None, columnv3=None, column4=None, columnv4=None):
    insert_statement1 = f"INSERT INTO {table} ({column1}, {column2} "
    if column3 is not None:
        insert_statement1 += f",{column3} "
    if column4 is not None:
        insert_statement1 += f",{column4}"
    insert_statement1 += f")"
    value_statement = f" VALUE({columnv1}, {columnv2} "
    if columnv3 is not None:
        value_statement += f",{columnv3} "
    if columnv4 is not None:
        value_statement += f",{columnv4}"
    value_statement +=f");"
    return insert_statement1 + value_statement

if len(column_list) == 2:
    print(insert(table, column1, columnv1, column2, columnv2))
elif len(column_list) == 3:
    print(insert(table, column1, columnv1, column2, columnv2, column3, columnv3))
elif len(column_list) == 4:
    print(insert(table, column1, columnv1, column2, columnv2, column3, columnv3, column4, columnv4))