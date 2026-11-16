"""
Variáveis constantes no python são declaradas em MAIÚSCULAS
Evitar muitas condições if no código
Quanto mais o código estiver afastado da margem esquerda pior
"""
velocidade = 61
local_carro = 101 #local da estrada KM

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1


velocidade_no_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_no_radar_1:
    print('Carro acima da velocidade permitida no radar 1')
if carro_passou_radar_1 and velocidade_no_radar_1:
    print('Carro acima da velocidade, carro multado no radar 1')

"""
if velocidade > RADAR_1:
    print('Carro acima da velocidade do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and (velocidade > RADAR_1):
    print('Carro multado no radar 1')
"""