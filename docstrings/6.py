def soma_divisores(numero:int) ->int :
    """
    :param numero:
    :return:numero + divisores
    """
    cont= 0
    for i in range (1, numero+1):
        if numero % i == 0:
            cont+= i
    return cont


print(soma_divisores(15))