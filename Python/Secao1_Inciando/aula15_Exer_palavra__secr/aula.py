"""
Faça um jogo para o usuário adivinhe qual é a palavra secreta
Vc vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar uma letra 
vc vai conferir se a letra digitada está na palavra
Se a letra digitada estiver na paravra exibe a letra
se a letra digitada não estiver adiciona um na contagem de chances
"""

palavra_secreta = 'Elefante'
palavra_secreta = palavra_secreta.lower()
palavra_oculta = '*' * len(palavra_secreta)

tentativas = 6
letras_usadas = []

while tentativas > 0 and "*" in palavra_oculta:
    print(f"Palavra: {palavra_oculta}")
    print(f"Tentativas Restantes: {tentativas}")
    print(f"Letras já Digitadas: {', ' .join(letras_usadas)}")
    chute = input("Digite uma Letra: ").lower().strip()

    if len(chute) != 1 or not chute.isalpha():
        print("Erro: Digite exatamente UMA letra apenas.")
        print("\n" + "=" * 75)
        continue
    if chute in letras_usadas:
        print("Erro: Você já tentou essa letra.")
        print("\n" + "=" * 75)
        continue
    letras_usadas.append(chute)
    if chute in palavra_secreta:
        print(f"Boa! A letra {chute} existe na palavra.")
        print("\n" + "=" * 75)
        for indice, letra in enumerate(palavra_secreta):
            if letra == chute:
                palavra_oculta = palavra_oculta[:indice] + chute + palavra_oculta[indice + 1:]
    else:
        tentativas -= 1
        print(f"A letra {chute} não está na palavra.")
        print("\n" + "=" * 75)
print("\n" + "=" * 75)
if "*" not in palavra_oculta:
    print(f"Parabéns! Você venceu! A palavra era: {palavra_secreta.upper()}")
else:
    print(f"Fim do Jogo! Suas tentativas acabaram! A palavra era: {palavra_secreta.upper()}")