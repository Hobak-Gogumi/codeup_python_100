n = int(input()) # 흰 돌의 개수 입력

d = [] # 바둑판 리스트(d) 선언

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(n):
    a, b = input().split()

    a = int(a)
    b = int(b)

    d[a][b] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()