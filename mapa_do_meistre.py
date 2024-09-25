largMap = int(input())
altMap = int(input())
mapa = []
for i in range(altMap):
    mapa.append(input())
i, j, cont = 0, 0, 0
lastOne = mapa[0][0]
if altMap != 1:
    while i < largMap:
        cont += 1
        if mapa[j][i] != ".":
            lastOne = mapa[j][i]
        if cont == altMap * largMap:
            print("!")
            exit()
        elif j == altMap:
            print("!")
            exit()
        match lastOne:
            case ">":
                i += 1
            case "<":
                i -= 1
            case "v":
                j += 1
            case "^":
                j -= 1
            case "*":
                print("*")
                exit()
    print("")
else:
    while i < largMap:
        cont += 1
        if mapa[0][i] != ".":
            lastOne = mapa[0][i]
        if i == altMap * largMap:
            print("!")
            exit()
        match lastOne:
            case ">":
                i += 1
            case "<":
                i -= 1
            case "v":
                j += 1
            case "^":
                j -= 1
            case "*":
                print("*")
                exit()
    print("!")