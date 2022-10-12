num = int(input())

for a in range(num):
    linha = []
    for b in range(1, a+2):
        linha.append(str(b))
    print(" ".join(linha))
