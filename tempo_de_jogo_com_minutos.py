hrInic, minInic, hrFinal, minFinal = map(int, input().split())
hrDiff = hrFinal - hrInic
minDiff = minFinal - minInic
if hrDiff < 0:
    hrDiff = 24 + hrDiff
if hrDiff == 0 and minDiff <= 0:
    hrDiff = 24
if minDiff < 0:
    hrDiff -= 1
    minDiff += 60
print(f"O JOGO DUROU {hrDiff} HORA(S) E {minDiff} MINUTO(S)")