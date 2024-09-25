n = int(input())
tab = n*n
if n % 2 == 0:
    cb = cp = tab//2
else:
    cb = 1+(tab//2)
    cp = tab//2
print(f"{cb} casas brancas e {cp} casas pretas")