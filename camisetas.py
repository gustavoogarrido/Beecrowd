n = int(input())
cont = 0
while(n != 0):
    corTam = {"branco P": [], "branco M": [], "branco G": [], "vermelho P": [], "vermelho M": [], "vermelho G": []}
    if cont != 0:
        print()
    listaPes = []
    for i in range(n):
        pessoas = input()
        camisa = input()
        corTam[camisa].append(pessoas)
    for key in corTam:
        corTam[key].sort()
    for key in corTam:
        for i in range(len(corTam[key])):
            print(key, end=" ")
            print(corTam[key][i])
    n = int(input())
    cont += 1