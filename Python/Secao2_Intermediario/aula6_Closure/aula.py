"""
Closure é uma função que retorna outra função

"""

def criar_sadacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_sadacao('Bom dia')

s2 = criar_sadacao('Bom Noite')
print(s1('Robson'))
print(s2('Luis'))