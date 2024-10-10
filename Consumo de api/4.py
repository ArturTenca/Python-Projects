"""
A API abaixo retorna um JSON com as informações de 100 produtos. Faça um
programa que consulte a API e informe o valor total do estoque (somatório de todos
os produtos). Considere que cada produto possui um preço (price), um desconto
(discountPercentage) que deve ser aplicado ao preço de cada produto e uma
quantidade de itens em estoque (stock).
http://dummyjson.com/products?limit=100
"""

import requests

response = requests.get(f'http://dummyjson.com/products?limit=100')

if response.status_code == 200:
    dados = response.json()
    total = 0
    for i in range (len(dados['products'])):
        preco = dados['products'][i]['price']
        desconto = dados['products'][i]['discountPercentage']
        estoque = dados['products'][i]['stock']
        porcentagem = (preco * desconto) / 100
        total += (preco - porcentagem) * estoque
    print(total)
