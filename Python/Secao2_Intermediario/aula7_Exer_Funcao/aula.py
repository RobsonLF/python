"""
Exercícios
Crie funções que duplicam, triplicam, quadruplicam o número recebido como parâmetros


def duplicar(numero):
    return numero * 2
"""

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(duplicar(4))
print(triplicar(4))