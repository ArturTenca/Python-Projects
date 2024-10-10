"""
A API abaixo retorna um JSON com informações de 50 receitas culinárias. Faça um
programa que consulte a API e exiba todas as receitas que utilizam um determinado
ingrediente informado pelo usuário.
http://dummyjson.com/recipes?limit=50
"""

import requests

response = requests.get('https://dummyjson.com/recipes?limit=50')

ing = input('de um ingrediente')

if response.status_code == 200:
    dados = response.json()
    for i in range(len(dados['recipes'])):
        if ing in dados['recipes'][i]['ingredients']:
            print(dados['recipes'][i]['name'])
