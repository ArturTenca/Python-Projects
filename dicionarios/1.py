def pessoas ():
    pessoas = {}
    for i in range (5):
        cpf = int(input('de o cpf de uma pessoa:'))
        nome = input('de o nome da pessoa:')
        pessoas[cpf] = nome
    return print(pessoas)

pessoas()