"""
Crie dois sets, um com números pares e outro com números ímpares. Os números
devem variar de 1 a 10.
o União: Obtenha a união dos dois sets.
o Interseção: Obtenha a interseção dos dois sets.
o Diferença: Obtenha a diferença dos sets (elementos que estão no primeiro set
e não no segundo).
"""

set1 = {1,3,5,7,9,5,6,8,}
set2 = {2,4,6,8,10,1,2,9}

uniao = set1.union(set2)
print(uniao)

interseccao = set1.intersection(set2)
print(interseccao)

diferenca1 = set1.difference(set2)
print(diferenca1)

diferenca2 = set2.difference(set1)
print(diferenca2)
