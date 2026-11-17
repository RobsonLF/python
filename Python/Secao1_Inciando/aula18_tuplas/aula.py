lista = ['Robson','Annelisa','Esther','Luísa']

nome1, nome2, nome3, nome4 = lista

nome11, *resto = lista
nome111, *_ = lista

_, nome22, *_  = lista
_, _, nome33, *_ = lista

#print(nome33 )

#tuplas - É uma lista imutável
listaTupla = 'Robson','Annelisa','Esther','Luísa'

print(type(listaTupla))