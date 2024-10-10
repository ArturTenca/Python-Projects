"""
A PokeAPI é uma API pública que fornece acesso a dados sobre o universo Pokémon. Ela
permite que desenvolvedores e entusiastas acessem informações sobre Pokémon,
movimentos, tipos, habilidades, evoluções e muito mais.
A URL http://pokeapi.co/api/v2/pokemon/ é o endpoint da PokeAPI que retorna uma lista de
Pokémon. Quando você faz uma requisição para essa URL, recebe um objeto JSON contendo
informações sobre vários Pokémon, incluindo seus IDs, nomes e links para detalhes
adicionais.
A API divide os resultados em várias páginas, para isso, o JSON apresenta a chave "next" que
indica a URL do próximo conjunto de resultados na lista de Pokémon.
Por exemplo, se a resposta contiver um "next" que aponta para uma nova URL, você pode
fazer uma nova requisição para essa URL para obter os próximos Pokémon na sequência. Se
não houver mais Pokémon para mostrar, o valor de "next" será null. Isso permite que você
navegue pelos resultados de forma eficiente.
Implemente uma aplicação para realizar consultas a essa API e listar os nomes de todos os
Pokémon.
Atualmente, a PokeAPI lista 1302 Pokémon (esse número pode mudar com novos
lançamentos ou atualizações na franquia, mas esse é o total mais recente)
"""
import requests
n = 0
while True:
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/?offset={n}&limit=20')
    if response.status_code == 200:
        dados = response.json()
        for i in range(len(dados['results'])):
            print(dados['results'][i]['name'])

    n += 20
