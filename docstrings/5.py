def calcular_salario (salario:float)->float :
    """
    :param salario:
    :return: salario ajustado
    """
    if salario > 2000:
        ajuste = salario + ((salario / 100) * 7)
    else:
        ajuste = salario + ((salario / 100) * 15)

    return ajuste



print(calcular_salario())