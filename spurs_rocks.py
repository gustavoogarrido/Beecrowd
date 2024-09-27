class time:
    def __init__(self, insc, ponto, pontoRec, victory, loses):
        self.insc = insc
        self.ponto = ponto
        self.pontoRec = pontoRec
        self.victory = victory
        self.loses = loses
    def addPoints(self, ponto):
        self.ponto += ponto
    def addReceived(self, pontoRec):
        self.pontoRec += pontoRec
    def addVictory (self, victory):
        self.victory += victory
    def addLost (self, loses):
        self.loses += loses
    def getTotalPoints(self):
        return self.loses + self.victory
    def cestaAverage(self):
        if self.pontoRec != 0:
            return self.ponto / self.pontoRec
        else:
            return self.ponto

qtdtimes = int(input())
cont = 0
while qtdtimes != 0:
    if cont != 0:
        print()
    cont += 1
    teams = []
    for i in range(qtdtimes):
        teams.append(time(i, 0, 0, 0, 0))
    for i in range(int(qtdtimes * (qtdtimes - 1) / 2)):
        time1, pontos1, time2, pontos2 = [int(x) for x in input().split()]
        teams[time1 - 1].addPoints(pontos1)
        teams[time1 - 1].addReceived(pontos2)
        teams[time2 - 1].addPoints(pontos2)
        teams[time2 - 1].addReceived(pontos1)
        if pontos1 > pontos2:
            teams[time1 - 1].addVictory(2)
            teams[time2 - 1].addLost(1)
        else:
            teams[time2 - 1].addVictory(2)
            teams[time1 - 1].addLost(1)
    classif = sorted(teams, key=lambda x: (-x.getTotalPoints(), -x.cestaAverage(), -x.ponto, x.insc))
    print(f"Instancia {cont}")
    j = 0
    for i in classif:
        j += 1
        if j == len(classif):
            print(i.insc + 1)
        else:
            print(i.insc + 1, end=" ")
    qtdtimes = int(input())