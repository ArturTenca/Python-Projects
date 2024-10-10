def listaa () ->str:
    lista =[]

    for i in range(10):
        numero = int(input('de um numero:'))
        lista.append(numero)

    contpares = 0
    for par in lista:
        if par % 2 == 0:
            contpares += 1

    somaimpares = 0
    for impar in lista:
        if impar % 2 != 0:
            somaimpares += impar

    return print(f'quantidade de pares na lista: {contpares}\n'
                 f'somatorio dos impares: {somaimpares}')


listaa()