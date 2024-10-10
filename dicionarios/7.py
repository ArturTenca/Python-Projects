"""
Exercício 3
Crie um dicionário chamado 'estoque' com informações sobre alguns produtos:
- Chave: Nome do produto
- Valor: Tupla contendo preço e quantidade em estoque
Adicione pelo menos 5 produtos ao dicionário.
Crie uma função chamada 'total_valor_estoque' que calcula o valor total do estoque (preço * quantidade) para
todos os produtos no dicionário.
Exemplo da estrutura a ser criada:
estoque = {'caneta': (4.70, 40), 'caderno': (45.0, 20), 'lápis': (3.50, 10)}
"""


def valor_total_estoque (estoque:dict) :
    for chave, valor in estoque.items():
        print(f'{chave}:{valor[0] * valor[1]} R$')

loja = {'caneta': (4.70, 40), 'caderno': (45.0, 20), 'lápis': (3.50, 10), 'borracha': (3.0, 20), 'lapiseira': (12.0, 20)}
valor_total_estoque(loja)