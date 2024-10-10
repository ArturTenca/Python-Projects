def list ():
    listapar = []
    listaimpar = []
    for i in range (10):
        n = int(input('digite um numero'))
        if n % 2 == 0:
            listapar.append(n)
        else:
            listaimpar.append(n)

    return print(f'{listapar}\n {listaimpar}')

list()