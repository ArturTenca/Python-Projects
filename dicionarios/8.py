"""
Crie um dicionário chamado pessoas que contenha informações sobre pessoas.
- Chave: cpf da pessoa
- Valor: dicionário contendo nome, idade e cidade.
Adicione pelo menos 5 pessoas ao dicionário.
Crie uma função chamada 'pessoas_cidade' que exibe o nome de todas as pessoas que moram em uma
cidade específica.
Exemplo da estrutura a ser criada:
pessoas = {
'123.888.999-89': {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'},
'845.678.658-02': {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'},
'555.781.657-12': {'nome': 'Eva', 'idade': 22, 'cidade': 'São Paulo'}
"""


def pessoas_cidade(pessoas:dict):
    uf = input('digite a cidade que deseja')

    for chave, valor in pessoas.items():
        if uf == valor['cidade']:
            print(valor['nome'])


pessoas = {
'123.888.999-89': {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'},
'845.678.658-02': {'nome': 'Bob', 'idade': 30, 'cidade': 'Rio de Janeiro'},
'555.781.657-12': {'nome': 'Eva', 'idade': 22, 'cidade': 'São Paulo'}
}
pessoas_cidade(pessoas)