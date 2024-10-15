"""
Considere que o arquivo “notas.txt” apresenta uma listagem com os dados dos alunos de uma turma. Cada linha
do arquivo apresenta os dados de um aluno, no formato:
RM,NOME,NOTA1,NOTA2,NOTA3,NOTA4
Veja abaixo um exemplo de arquivo de texto nesse formato

Implemente um programa que leia o arquivo indicado e, a partir desse arquivo, gere dois novos arquivos:
• Arquivo “aprovados.txt” contendo uma listagem dos alunos aprovados na disciplina, contendo
RM,NOME,MEDIA do aluno
• Arquivo “reprovados.txt” contendo uma listagem dos nomes dos alunos reprovados na disciplina,
contendo RM,NOME,MEDIA do aluno.
Para o aluno ser aprovado ele deve ter média igual ou superior a 6.0
"""
from idlelib.replace import replace

with open('notas.txt', 'r', encoding='UTF-8') as notas:
    with open('aprovados.txt', 'w', encoding='UTF-8') as aprov:
        with open('reprovados.txt', 'w', encoding='UTF-8') as reprov:
            lista = []
            for linha in notas:
                palavras = linha.replace("\n", "").split(",")
                lista = palavras[-4:]
                soma_notas = []
                for i in range(len(lista)):
                    soma_notas.append(float(lista[i]))
                media = (sum(soma_notas)) / 4
                print(palavras)
                if media >= 6:
                    aprov.write(f'{palavras[0]},{palavras[1]},{str(media)}\n')
                elif media <= 6:
                    reprov.write(f'{palavras[0]},{palavras[1]},{str(media)}\n')

