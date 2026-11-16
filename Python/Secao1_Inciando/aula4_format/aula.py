a = 'A'
b = 'B'
c = 1.1


string = 'a={0} b={1} c={2:.2f}'.format(a,b,c)
string1 = 'a={nome1} b={nome2} c={nome3:.2f}' #argumentos nomeados
formato = string.format(a,b,c)
formato1 = string1.format(nome1=a,nome2=b,nome3=c)


print(formato)
print(formato1)
