"""
Solicite ao usuário diversos números inteiros (até que seja digitado o número zero). Armazene os
números pares em um arquivo e os números ímpares em outro arquivo.
"""

with open ('par.txt', 'w', encoding='UTF-8') as par:
    with open ('impar.txt', 'w', encoding='UTF-8') as impar:
        while True:
            try:
                num = int(input('digite um numero:'))
                if num % 2 == 0:
                    par.write(f'{num}\n')
                else:
                    impar.write(f'{num}\n')
            except ValueError:
                print('\nFim do porgrama')
                break