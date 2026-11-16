"""
Exercício
Peça ao usuário para digitar o nome
Peça ao usuário para digitar a idade
Se o nome e a idade forem digitados:
Exiba 
    Seu nome é: <nome>
    Seu nome invertido é:
    Seu nome contém ou não espaçosR
    seu nome tem {n} letras
    A ultima letra do seu nome é: <letra>
Se nada for digitado 
    "Desculpe, você deixou campos vazios".

"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

if nome and idade:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome invertido é: {nome[::-1]}")
    if " " in nome:
        print("Seu nome contém espaços.")
    else:
        print("Seu nome não contém espaços.")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A última letra do seu nome é: {nome[-1]}")
else:
    print("Desculpe, você deixou campos vazios.")