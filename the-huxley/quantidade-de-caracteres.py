def contador(caracter):
    contar = 0
    for i in caracter:
        contar = contar + 1
    return contar

s = str(input())
print(contador(s))
