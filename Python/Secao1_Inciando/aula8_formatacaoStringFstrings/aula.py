"""
Interpolação básica de strings
s -string
d - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
(caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel:#>10}')
print(f'{variavel:.<10}')
print(f'{variavel:$^100}')
print(f'{1000.5645678646546546:.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')


