t = int(input())
for c in range(t):
    a, b = [int(x) for x in input().split()]
    a = str(a)
    b = str(b)
    tam = len(a) - len(b)
    if b in a[tam:]:
        print("encaixa")
    else:
        print("nao encaixa")