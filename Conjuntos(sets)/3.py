"""
Dada uma lista com vários elementos (alguns podem ser duplicados), crie um set a
partir dessa lista e conte a quantidade de elementos únicos.
"""

lista = [1,1,2,2,3,2,3,4,3,4,5,4,5,6,7,8,9,9,7,8,7,7,6,5,6,8,8,10]

lista_set = set(lista)
print(lista_set)
cont =0
for i in range(len(lista_set)):
    cont += 1
print(f'o set possui {cont} itens')