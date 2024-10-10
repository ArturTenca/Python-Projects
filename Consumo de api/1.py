"""
Solicite ao usuário a sigla de uma UF e utilize a API abaixo para consultar e exibir os
nomes de todos os municípios da UF informada.
http://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios
"""

import requests
uf = input('de a sigla de um estado:')
response = requests.get(f'https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios')

if response.status_code == 200:
    dados = response.json()
    for i in dados:
        print(i['nome'])