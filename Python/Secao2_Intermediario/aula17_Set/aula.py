"""
Sets - Conjuntos em python (tipo set)
Conjuntos são ensinados na matemática
Representado graficamente pelo diagrama de venn
Sets em python são mutáveis, porém aceitam apenas tipos imutaveis como valor interno

criando um set

set(iteravel) ou {1,2,3}

Sets são eficientes para remover valores duplicados de iteráveis
- eles não tem indexes
- eles não garantem ordem
- eles são iteraveis (for, in, not in)
Métodos úteis
add, update, clear, discard

Operadores uteis
união | union
intersecção &  Itens presentes em ambos 
diferença - Itens presentes apenas no set da esquerda
direrença simétrica ^ - Itens que não estão em ambos os sets

"""

#s1 = set('Robson')
"""
l1 = [1,2,3,3,3,3,1]

s1 = set(l1)
l2 = list(s1)
print(l2)

for num in s1:
    print(num)
"""

"""
s1 = set()
s1.add(1)
s1.add('Robson')
s1.add(2)

s1.update(('Olá mundo', 1,2,3,4))
s1.discard('Olá mundo')
#s1.clear()

print(s1)

"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2

print(s3)
print(s4)
print(s5)
print(s6)