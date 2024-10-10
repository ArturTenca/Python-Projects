"""
Escreva um programa que recebe uma frase como entrada e retorna um dicionário onde as chaves são as
palavras únicas na frase e os valores são o número de vezes que cada palavra aparece.
Exemplo:
Para o texto abaixo:
'Exemplo de texto para contagem de palavras no texto'
Deve ser gerado o dicionário:
{'Exemplo': 1, 'de': 2, 'texto': 2, 'para': 1, 'contagem': 1, 'palavras': 1, 'no': 1}
"""


text = input('de um texto')
texto = text.split()
dicionario = {}
for i in texto:
    ii = i.lower()
    if ii in dicionario.keys():
        dicionario[ii] += 1
    else:
        dicionario[ii] = 1

print(dicionario)