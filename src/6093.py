n = int(input()) # 번호를 부른 횟수

a = input().split() # n개의 랜덤 번호 입력

for i in range(n):
    a[i] = int(a[i])

for i in range(n - 1, -1, -1):
    print(a[i], end = " ")