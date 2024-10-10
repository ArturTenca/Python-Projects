def conta_vogais(texto: str) -> int:
    """Retorna a quantidade de vogais existentes em uma string"""
    cont = 0
    vogais = 'aeiou'
    for caracter in texto:
        if caracter.lower() in vogais:
            cont += 1
    return print(f'Quantidade de vogais: {cont}')


conta_vogais('abcde')
