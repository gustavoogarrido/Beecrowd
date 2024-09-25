t = int(input())
for c in range(t):
    qtdtimes, jogos = [int(x) for x in input().split()]
    fed = {}
    times = []
    for i in range(qtdtimes):
        fed[input()] = [0, 0, 0]
    gols1 = 0
    gols2 = 0
    cont = 0
    for i in range(jogos):
        jogo = []
        time, ponto = [0] * qtdtimes, [0] * qtdtimes
        ponto[0], time[0], ponto[1], time[1] = input().split()
        fed[time[0]][2] += int(ponto[0])
        fed[time[1]][2] += int(ponto[1])
        # arrumar (botar os bgl do for de baixo aqui em cima)
    for key, values in fed.items():
        empate = ponto[0] == ponto[1]
        vit1 = ponto[0] > ponto[1]
        pontuacao1 = 0
        pontuacao2 = 0
        vitorias1 = 0
        vitorias2 = 0
        if key == time[0]:
            gols1 += int(ponto[0])
            if empate:
                pontuacao1 += 1
            elif vit1:
                if key == time[0]:
                    pontuacao1 += 3
                    vitorias1 += 1
            values[0] = pontuacao1
            values[1] = vitorias1
            values[2] = gols1
            fed[key] = [values]
        else:
            gols2 += int(ponto[1])
            if empate:
                pontuacao2 += 1
            elif vit1:
                if key == time[0]:
                    pontuacao2 += 3
                    vitorias2 += 1
            values[0] = pontuacao2
            values[1] = vitorias2
            values[2] = gols2
            fed[key] = [values]
    fed = list(fed.items())
    print(fed)
    fed = sorted(fed, key=lambda x: (x[1][0][0], x[1][0][1], x[1][0][2]), reverse=True)
    print(fed)
    for i in range(qtdtimes):
        print(fed[i][0])