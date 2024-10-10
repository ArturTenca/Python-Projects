'''
Utilize a API abaixo para gerar uma listagem com os nomes de N usuários. Exiba a
lista em ordem alfabética
http://randomuser.me/api/?results={n}
'''

import requests
n = int(input('de o numero de usuários:'))
for i in range (0, n):
    response = requests.get(f'http://randomuser.me/api/?results={n}')
    if response.status_code == 200:
        dados = response.json()
        for a in range(len(dados['results'])):
            print(f'{dados['results'][a]['name']['title']} '
                  f'{dados['results'][a]['name']['first']} '
                  f'{dados['results'][a]['name']['last']} ')