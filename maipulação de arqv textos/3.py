"""
Faça um programa que crie um arquivo de texto denominado “arquivo.txt” e permita que o usuário
grave diversos caracteres nesse arquivo até que seja digitado o caractere “0” (zero).
"""

with open ('arquivo.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        a = input('digite um caracter')
        if a == '0':
            break
        else:
            arquivo.write(f'{a}\n')
