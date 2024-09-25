teste = int(input())
for i in range(1, teste + 1):
    n, k = [int(x) for x in input().strip().split(' ')]
    pessoa = 0
    for j in range(1, n + 1):
        pessoa = (pessoa + k) % j
    print(f"Case {i}: {pessoa + 1}")