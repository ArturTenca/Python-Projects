"""
Dado dois sets, obtenha a diferença simétrica, ou seja, os elementos que estão em um
dos sets, mas não em ambos.
"""

set1 = {'a','b','c','d'}
set2 = {'b', 'd'}

set3 = set1.difference(set2)
print(f"a diferenca é:{set3}")