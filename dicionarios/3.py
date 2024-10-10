"""
Preencha um dicionário com os dados de 5 alunos.
- Utilize o RM do aluno como chave e uma lista de três notas como valor.
- Solicite os dados ao usuário.
Percorra o dicionário e exiba a média de cada aluno.
Exemplo:
Veja um exemplo da estrutura do dicionário.
{1901502: [10, 8, 7.5], 2002441: [6, 5, 7.5], 2001332: [5, 8, 9.5]}
"""


def calcular_medias(alunos: dict) -> None:
    for rm, notas in alunos.items():
        media = sum(notas) / len(notas)
        print(f'Aluno de RM {rm} obteve média {media:.2f}')

def cadastrar_notas() -> dict:
    alunos = {}
    for _ in range(5):
        rm = input('RM: ')
        lista = []
        for j in range(3):
            n = float(input(f'Nota {j+1}: '))
            lista.append(n)
        alunos[rm] = lista
    return alunos

alunos = cadastrar_notas()
calcular_medias(alunos)