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

cpf_limpo = re.sub(r"\D","",cpf_string)

if len(cpf_limpo) == 11:

else:
    print("CPF inválido. Insirá novamente!")