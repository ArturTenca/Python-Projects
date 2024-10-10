"""
Abra o arquivo de texto criado no exercício anterior. Leia o conteúdo do arquivo e mostre o somatório
de todos os números contidos no arquivo
"""

with open('arquivo1.txt', 'r', encoding='UTF-8') as arquivo:
    cont = 0
    for i in arquivo:
        i_int = int(i)
        cont += i_int
    print(cont)