
"""
Escopo de uma função em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e local
o Escopo global é o escopo onde todo o código é alcançavel
O Escopo local é o escopo onde apenas nomes do mesmo local podem ser acessados

"""
x = 1

def escopo():
    print(x)

escopo()