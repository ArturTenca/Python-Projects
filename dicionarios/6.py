"""
Exercício 2
Crie uma lista de tuplas, onde cada tupla contém informações sobre um aluno:
(Nome do aluno, Idade, Nota)
Escreva uma função chamada 'alunos_aprovados' que recebe a lista de alunos e retorna uma nova lista apenas
com os nomes dos alunos que têm uma nota maior ou igual a 7.
Exemplo da estrutura a ser criada:
alunos = [('Alice', 20, 8.5), ('Bob', 18, 5.0), ('Eva', 22, 7.5)]
Exemplo de Retorno:
['Alice', 'Eva']
"""


def alunos_aprovados (alunos) :
    for i in range(len(alunos)):
        if alunos[i][2] >= 7:
            print(alunos[i][0])


alunos = [('Alice', 20, 8.5), ('Bob', 18, 5.0), ('Eva', 22, 7.5),('João', 18, 9)]
alunos_aprovados(alunos)