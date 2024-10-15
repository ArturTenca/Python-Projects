"""
Faça um programa que abra os dois arquivos criados no exercício anterior e copie-os para um novo
arquivo, colocando-os em ordem crescente.
"""

with open ('notas_alunos.txt','w',encoding='UTF-8') as notas:
    while True:
        nome = input('de o nome do aluno:')
        if nome == '':
            break
        n1 = float(input('de a nota 1:'))
        n2 = float(input('de a nota 2:'))
        n3 = float(input('de a nota 3:'))
        n4 = float(input('de a nota 4:'))

        notas.write(f'{nome}: nota 1:{n1} nota 2:{n2} nota 3:{n3} nota 4:{n4} média:{f'{(n1 + n2 + n3 + n4)/4 :.2}'}\n')


