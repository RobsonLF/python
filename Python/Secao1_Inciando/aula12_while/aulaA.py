nome='Robson Luis David Ferreira'
nome_novo = ''
tamanho = len(nome)
cont = 0
while cont < tamanho:
    letra = ''
    letra = '*' + nome[cont]
    nome_novo = nome_novo + letra
    cont += 1

print(nome_novo)