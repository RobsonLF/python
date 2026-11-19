"""
Exercício com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o tottal para uma variável e mostre o valor da variável
Crie uma função que fale se um número é para ou impar
Retorne se o número é par ou impar

"""


def multiplicador(*args): #*args é usado quando os quando não tem definido a quantidade de argumentos que serão passados na função
    acumulador = 1
    for num in args:
        acumulador  *= num
    return acumulador

multip = multiplicador(1,2,3,4,5)
print(multip)

def par_impar(numero):
    modulo_numero = numero % 2 == 0

    if modulo_numero:
        return f'{numero} é par!!'
    return f'{numero} é impar!!'

print(par_impar(11))