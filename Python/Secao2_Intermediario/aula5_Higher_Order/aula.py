"""
Higher order functions
Funções de primeira classe

"""


def saudacao(msg):
    return msg

def executa(funcao):
    return funcao()

v = saudacao('Bom dia')
print(v)

saudacao_2 = saudacao
