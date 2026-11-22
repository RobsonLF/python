

perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2 ?',
        'Opções': ['1','2','3','4','5'],
        'Resposta': '4',
    },
    {
        'Pergunta':'Quanto é 5 * 5 ?',
        'Opções':['25','55','10','50'], 
        'Resposta':'25',
    },
    {
        'Pergunta':'Quanto é 10 / 2 ?',
        'Opções':['4','5','2','1'],
        'Resposta':'5',
    },
]
for pergunta in perguntas:
    print('pergunta', pergunta['Pergunta'])
    print()
    
    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{indice})',opcao)
    print()
    escolha = input('Escolha uma opção: ')

    print()
