"""
Algoritmo CPF
 746.824.890-70
Primeiro dígito
    10    9    8    7    6    5    4    3    2 
*   7     4    6    8    2    4    8    9    0
    70    36   48   56   12   20   32   27   0 

    11 - (301 % 11) = 7 se resultado maior que 10 o dígito é 0

Segundo Digito
    11    10    9    8    7    6    5    4    3    2
    7     4     6    8    2    4    8    9    0    7
    77    40    54   64   14   24   40   36   0    14

    11 - (363 % 11) = 11 se resultado maior que 10 o dígito é 0 

"""
import re

cpf_string = "746.824.890-70"

#cpf_limpo = re.sub(r"\D","",cpf_string)
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