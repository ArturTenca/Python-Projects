"""
Considere que o arquivo “ips.txt” apresenta uma listagem com os endereços IPs que acessaram um site.
Veja abaixo um exemplo de arquivo de texto nesse formato

A partir desse arquivo, gere um novo arquivo com uma listagem de IPs únicos (sem valores repetidos).
"""

with open('ips_norep.txt', 'w', encoding='UTF-8') as ips_norep:
    with open('ips.txt', 'r', encoding='UTF-8') as ips:
        ips_list = []
        for i in ips:
            ii = i.replace('\n', '')
            ips_list.append(ii)
            ips_conj = set(ips_list)
        for a in ips_conj:
            ips_norep.write(f'{a}\n')