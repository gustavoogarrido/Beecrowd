n = int(input())
for i in range(n):
    verif = 0
    jafoi = 0
    dieta = input()
    cafe = input()
    almoco = input()
    if cafe is not None:
        for k in range(len(cafe)):
            verif = 0
            for j in range(len(dieta)):
                if cafe[k] == dieta[j]:
                    dieta = dieta.replace(dieta[j], "")
                    verif = 1
                    break
            if verif == 0:
                print("CHEATER")
                jafoi = 1
                break
    if jafoi != 1 and almoco is not None:
        for y in range(len(almoco)):
            verif = 0
            for j in range(len(dieta)):
                if almoco[y] == dieta[j]:
                    dieta = dieta.replace(dieta[j], "")
                    verif = 1
                    break
            if verif == 0:
                jafoi = 1
                print("CHEATER")
                break
    if jafoi != 1:
        dieta = sorted(dieta)
        resultado = ''.join(map(str, dieta))
        print(resultado)