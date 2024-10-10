
nomes = []
idades = []

while True:
    nome = str(input('de um nome:'))
    if nome == '':
        break

    idade = int(input("Informe a idade: "))


    nomes.append(nome)
    idades.append(idade)

print("Pessoas com 18 anos ou mais:")
for i in range(len(nomes)):
    if idades[i] >= 18:
        print(nomes[i])
