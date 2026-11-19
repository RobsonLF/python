pessoa = {
    'nome':'Robson',
    'sobrenome':'Ferreira',
    'idade': 45,
    'altura':1.8,
    'endereco':[
        {
         'rua':'talta',
         'numero':1144
         },
        {
        'rua':'outra rua',
        'numero':'152'
        }
        ],
}
#print(pessoa['nome'])
#print(pessoa['sobrenome'])

for chave in pessoa:
    print(chave, pessoa[chave])