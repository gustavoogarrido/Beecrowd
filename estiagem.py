import math

imoveis = int(input())
cidades = {}
cont = 0
while imoveis != 0:
    cont += 1
    somaPessoas = 0
    somaConsumo = 0
    output1 = ""
    pessCons = []
    ordenado = []
    for t in range(imoveis):
        pessoas, consumo = [int(x) for x in input().split()]
        pessCons.append((pessoas, consumo))
        ordenado = sorted(pessCons, key=lambda x: x[0]/x[1])
        somaPessoas += pessoas
        somaConsumo += consumo
    output2 = f"O consumo medio: {somaConsumo/somaPessoas}"
    print(f"Cidade#{cont}:")
    tam = len(ordenado)
    for i in range(tam):
        if i + 1 == tam:
            output1 += f"{ordenado[i][0]}-{math.floor(ordenado[i][1]/ordenado[i][0])}"
        else:
            output1 += f"{ordenado[i][0]}-{math.floor(ordenado[i][1]/ordenado[i][0])} "
    print(output1)
    print(f"{output2} m3.")
    if cont != 0:
        print()
    imoveis = int(input())