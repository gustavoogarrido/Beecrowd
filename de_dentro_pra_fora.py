n = int(input())
for i in range(n):
    frase = input()
    resultado = ""
    size = len(frase)/2
    for j in range(int(size) - 1, -1, -1):
        resultado += frase[j]
    for j in range(len(frase) - 1, int(size) - 1, -1):
        resultado += frase[j]
    print(resultado)