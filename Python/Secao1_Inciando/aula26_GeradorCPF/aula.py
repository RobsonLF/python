import random
import re
import sys


for i in range(100):
    cpf_limpo = ''
    for i in range(9):
        cpf_limpo += str(random.randint(0,9)) 
    acumulador = 0
    #Calculo do Primeiro digito

    if len(cpf_limpo) == 9:
        multiplicador = 10
        for num in cpf_limpo:
            if multiplicador >= 2:
                acumulador = acumulador + (int(num) * multiplicador)
                multiplicador -= 1
        primeiro_digito = 11 - (acumulador % 11)
        if primeiro_digito >= 10:
            primeiro_digito = 0
        cpf_com_primeiro_digito = cpf_limpo[0:9] + str(primeiro_digito)
        #Calculo do Segundo Digito
        multiplicador = 11
        acumulador = 0
        for num in cpf_com_primeiro_digito:
            if multiplicador >= 2:
                acumulador = acumulador + (int(num) * multiplicador) 
                multiplicador -= 1
            segundo_digito = 11 - (acumulador % 11)
            if segundo_digito >= 10:
                segundo_digito = 0
        
        cpf_com_segundo_digito = cpf_com_primeiro_digito + str(segundo_digito)
        cpf_novo = cpf_com_segundo_digito[0:3] + '.' + cpf_com_segundo_digito[3:6] + '.' + cpf_com_segundo_digito[6:9] + '-'+ cpf_com_segundo_digito[9:11]
        print(f'CPF novo {cpf_novo} gerado com sucesso!!!')
    else:
        print("CPF inválido. Insirá novamente!")




"""
cpf_string = "746.824.890-70"


#cpf_limpo = re.sub(r'[^0-9]','',cpf_string) o ^ excluir tudo que não for um numero e substitui por ""
cpf_limpo = cpf_string.replace('.','').replace('-','')
acumulador = 0
#Calculo do Primeiro digito
if len(cpf_limpo) == 11:
    multiplicador = 10
    for num in cpf_limpo:
        if multiplicador >= 2:
            acumulador = acumulador + (int(num) * multiplicador)
            multiplicador -= 1
    primeiro_digito = 11 - (acumulador % 11)
    if primeiro_digito >= 10:
        primeiro_digito = 0
    cpf_com_primeiro_digito = cpf_limpo[0:9] + str(primeiro_digito)
    #print(cpf_com_primeiro_digito)

    #Calculo do Segundo Digito
    multiplicador = 11
    acumulador = 0
    for num in cpf_com_primeiro_digito:
        if multiplicador >= 2:
            acumulador = acumulador + (int(num) * multiplicador) 
            multiplicador -= 1
        segundo_digito = 11 - (acumulador % 11)
        if segundo_digito >= 10:
            segundo_digito = 0
    
    cpf_com_segundo_digito = cpf_com_primeiro_digito + str(segundo_digito)

    if cpf_com_segundo_digito == cpf_limpo:
        print(f'O CPF {cpf_string} é um CPF válido!!!')
    else:
        print(f'O CPF {cpf_string} é um CPF inválido!!!')
else:
    print("CPF inválido. Insirá novamente!")

    """