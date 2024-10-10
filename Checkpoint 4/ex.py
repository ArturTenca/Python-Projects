"""
Crie um programa que simule um sistema de gerenciamento de estoque para uma loja. O programa deve utilizar um dicionário para armazenar as
informações, exatamente como ilustrado no exemplo abaixo.
As chaves são os nomes dos produtos e os valores são dicionários contendo a marca, o preço unitário e a quantidade em estoque.

O programa deve permitir ao usuário:
• adicionar novos produtos
• remover produtos existentes
• consultar as informações referente a um produto
• alterar o preço e a quantidade de um produto
• calcular o valor total do estoque
O programa deve disponibilizar um menu contendo as funcionalidades implementadas.
Deve ser disponibilizada uma opção no programa que permita ao usuário encerrar a execução do programa. Caso contrário, o programa deve
permanecer em um loop, permitindo a realização de novas operações.
A estrutura do programa deve ser organizada em funções. As funções devem apresentar docstring e anotações de tipo.
"""


def menu () -> None:
    """Função Menu que chama todas as outras funções"""
    while True:
        print(f'\n--------------------------------------------------------------------------------'
              f'\n\n1 - Adicionar um produto novo   \n'
              f'2 - Remover um produto existente    \n'
              f'3 - Consultar um Produto            \n'
              f'4 - Alterar Valores                 \n'
              f'5 - Calcular valor total de estoque \n'
              f'6 - Visualizar Dicionário           \n'
              f'7 - Sair                            \n'
              f'\n--------------------------------------------------------------------------------\n')
        menu = int(input('Digite uma opção:'))

        match menu:
            case 1:
                Adicionar_produto(estoque)
            case 2:
                Remover_produto(estoque)
            case 3:
                Consultar(estoque)
            case 4:
                Alterar(estoque)
            case 5:
                Calcular(estoque)
            case 6:
                print(f'\n{estoque}')
            case 7:
                break


def Adicionar_produto (dicionario:dict)-> None :
    """Adiciona um novo produto ao dicionário"""
    chave = input('de o nome produto:')
    marca = input('de a marca:')
    preco = float(input('de o preco:'))
    estoque = int(input('de a quantidade de estoque:'))
    dicionario[chave] = {'marca' : marca, 'preco': preco, 'quantidade': estoque}
    print(dicionario)


def Remover_produto(dicionario: dict) -> None:
    """Função que recebe o estoque (um dicionário)  como parâmetro e remove um produto dela de acordo com o usuário."""
    remocao = str(input('Digite o nome do produto que deseja remover: ')).strip().capitalize()
    if remocao in dicionario:
        estoque.pop(remocao)
        return print(f'\nItem {remocao} removido com sucesso!')
    else:
        return print(f'\nItem {remocao} não encontrado!')


def Consultar (dicionario: dict) -> None :
    """ Consulta um produto de escolha do usuário no dicionário"""
    produto = input('digite produto que quer consultar:')
    for chave, valor in dicionario.items():
        if chave == produto:
            print(f'\n{chave} {valor}')


def Alterar (dicionario:dict) -> None :
    """Altera o preco e quantidade de um produto de escolha do usuário """
    produto = input('Digite o produto que deseja alterar o preco e quantidade:')
    for i in dicionario.keys():
        if i ==produto:
            valor = float(input('digite o novo valor:'))
            quant = int(input('digite a nova quantidade:'))
            dicionario[i]['preco'] = valor
            dicionario[i]['quantidade'] = quant
    print(dicionario)


def Calcular(dicionario:dict) -> None :
    """ CAlcula o valor totaL de estoque de todos os produtos do dicionario"""

    for chave,valor in dicionario.items():
        valor_produto = dicionario[chave]['preco'] * dicionario[chave]['quantidade']
        print(f'{chave}: {valor_produto} R$')


estoque = {
    'Caneta': {'marca': 'Bic', 'preco': 10.0, 'quantidade': 50},
    'Caderno': {'marca': 'Tilibra', 'preco': 20.0, 'quantidade': 30},
    'Borracha': {'marca': 'Faber-Castell', 'preco': 5.0, 'quantidade': 40},
    'Lápis': {'marca': 'Faber-Castell', 'preco': 15.0, 'quantidade': 25},
    'Estojo': {'marca': 'Faber-Castell', 'preco': 12.0, 'quantidade': 35},
    'Calculadora': {'marca': 'Casio', 'preco': 30.0, 'quantidade': 10},
    'Lápis de Cor': {'marca': 'Faber-Castell', 'preco': 35.0, 'quantidade': 12},
    'Fita Adesiva': {'marca': 'Scotch', 'preco': 14.0, 'quantidade': 22},
    'Pincel': {'marca': 'Faber-Castell', 'preco': 40.0, 'quantidade': 8},
    'Bolsa': {'marca': 'Nike', 'preco': 95.0, 'quantidade': 32}
}

menu()