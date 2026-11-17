frase = 'Ola só que, coisa interessante'
lista_palavras = frase.split()
lista_frases = frase.split(',')
print(lista_palavras)
print(lista_frases)

for i, frase in enumerate(lista_frases):
    print(lista_frases[i].strip())

frase_unidas = ','.join(lista_frases)
print(frase_unidas)