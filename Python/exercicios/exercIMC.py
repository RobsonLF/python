#imc = peso / (altura * altura)

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso(kg): "))
altura = float(input("Digite sua altura(m): "))

imc = peso / (altura * altura)

print ("Olá '{}".format(nome))
print ("Você tem {:.2f} kg".format(peso))
print ("Sua altura é {:.2f} m".format(altura))
print ("Seu IMC é: {:.2f}".format(imc))


print ("Olá '{}', seu IMC é: {:.2f}".format(nome, imc))