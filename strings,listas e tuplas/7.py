def lista ():
    lista = []
    for i in range(10):
        numero = int(input('de um numero:'))
        lista.append(numero)
    maior = 0
    for i in lista:
        if i > maior:
            maior = i

    menor = 111111111
    for i in lista:
        if i < menor:
            menor = i

    media = 0
    for i in lista:
        media += i
        final = media /10
    return print(f'maior numero: {maior}\n'
                 f'menor numero: {menor}\n'
                 f'media: {final}')


lista()


