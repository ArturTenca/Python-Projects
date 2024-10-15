"""
Considere o arquivo “foods.txt”, onde cada linha possui três campos:
NAME,ID,FAVORITEFOOD
Veja abaixo um exemplo de arquivo de texto nesse formato:
Michael Johnson,3,steak
Emily Davis,4,ice cream
William Brown,5,pasta
Sarah Miller,6,tacos
Daniel Taylor,7,burgers
Escreve um programa que leia esse arquivo e informe o alimento preferido pela maioria das pessoas.
"""

with open ('foods.txt','r', encoding='UTF-8') as arquivo:
    lista = []
    for i in arquivo:
        ii = i.replace('\n','').split(',')
        lista.append(ii)
    comidas = []
    for x in range(len(lista)):
        comidas.append(lista[x][2])
    print(comidas)



