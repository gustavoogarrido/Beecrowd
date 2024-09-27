class times:
    def __init__(self, nome, pontos, vitorias, gols):
        self.nome = nome
        self.pontos = pontos
        self.vitorias = vitorias
        self.gols = gols
    def addPontos(self, pontos):
        self.pontos += pontos
    def addGols(self, gols):
        self.gols += gols
    def addVitorias(self, vitorias):
        self.vitorias += vitorias

t = int(input())
for e in range(t):
    qtdtimes, qtdjogos = [int(x) for x in input().split()]
    teams = []
    nomes = []
    for i in range(qtdtimes):
        nomeTime = input()
        nomes.append(nomeTime)
        teams.append(nomeTime)
        teams[nomes.index(nomeTime)] = times(nomeTime,0, 0, 0)
    for i in range(qtdjogos):
        gols1, time1, gols2, time2 = input().split()
        gols1 = int(gols1)
        gols2 = int(gols2)
        teams[nomes.index(time1)].addGols(gols1)
        teams[nomes.index(time2)].addGols(gols2)
        if gols1 == gols2:
            teams[nomes.index(time1)].addPontos(1)
            teams[nomes.index(time2)].addPontos(1)
        elif gols1 > gols2:
            teams[nomes.index(time1)].addPontos(3)
            teams[nomes.index(time1)].addVitorias(1)
        else:
            teams[nomes.index(time2)].addPontos(3)
            teams[nomes.index(time2)].addVitorias(1)
    placar = sorted(teams, key=lambda x: (-x.pontos, -x.vitorias, -x.gols))
    for i in range(qtdtimes):
        print(placar[i].nome)