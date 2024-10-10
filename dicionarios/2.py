"""
Preencha um dicionário com as informações de 5 produtos.
- Utilize o nome do produto como chave e o preço como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba o nome dos produtos com preço superior a R$ 50.00
Exemplo:
Veja um exemplo da estrutura do dicionário.
{'Caneta': 3.0, 'Pen Drive': 100.0, 'Teclado': 30.0}
"""


def produtos ():
    produtos = {}
    for i in range (5):
        nome = input('de o nome do produto:')
        valor =int(input('de o valor:'))
        produtos[nome] = valor
    for i in produtos.values():
        if i > 50:
            print(i)

produtos()

