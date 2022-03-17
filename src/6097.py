h, w = input().split()

h = int(h)
w = int(w)

p = []

# 세로 h, 가로 w인 격자판 생성(0으로 채우기)
for i in range(h):
    p.append([])
    for j in range(w):
        p[i].append(0)

# n = 막대의 개수
n = int(input())

# 막대의 길이, 방향, 좌표를 입력받기
# 방향은 가로:0, 세로:1
# 좌표는 막대의 가장 왼쪽(가로일 때), 혹은 위쪽(세로일 때)

# 여기서 주의할 점은 1,1 이면 판의 가장 왼쪽 위를 찍는것. 실제 파이썬에서는 0,0이 시작인 것에 유의
for i in range(n):
    l, d, x, y = input().split()

    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)

    # 방향 0이면 좌표 기준으로 길이만큼 오른쪽으로 찍는다
    # 방향 1이면 좌표 기준으로 길이만큼 아래쪽으로 찍는다
    if(d == 0):
        for i in range(l):
            p[x-1][y-1] = 1
            y = y + 1
    elif(d == 1):
        for i in range(l):
            p[x-1][y-1] = 1
            x = x + 1

for i in range(h):
    for j in range(w):
        print(p[i][j], end= " ")
    print()