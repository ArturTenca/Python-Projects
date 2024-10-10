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

