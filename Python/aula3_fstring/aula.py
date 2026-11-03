nome = 'Robson Ferreira'
altura = 1.75
peso = 90

imc = peso / (altura ** 2)

linha = f'{nome} tem {altura:.2f} de altura, pesa{peso:.2f} kg e seu IMC é {imc:.2f}'

print(linha)