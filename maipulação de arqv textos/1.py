"""
Solicite ao usuário 10 números inteiros e armazene-os em um arquivo de texto (um número em cada
linha).
"""

with open ('arquivo1.txt', 'w', encoding='UTF-8') as arquivo:
    for i in range(10):
        num = int(input('de um numero:'))
        arquivo.write(f'{num}\n')