"""
Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo
arquivo, colocando-os em ordem crescente.
"""

with open ('par_impar.txt','w', encoding='UTF-8') as par_impar:
    with open('par.txt', 'r', encoding='UTF-8') as par:
        with open('impar.txt', 'r', encoding='UTF-8') as impar:
            lista = []
            for i in par:
                ii = i.replace('\n','')
                iii = int(ii)
                lista.append(iii)
            for i in impar:
                ii = i.replace('\n','')
                iii = int(ii)
                lista.append(iii)
            conj =  set(lista)
            for i in conj:
                par_impar.write(f'{i}\n')

