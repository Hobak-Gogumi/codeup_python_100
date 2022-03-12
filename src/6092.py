n = int(input()) # 입력할 개수

a = input().split() # 입력받은 값을 저장

for i in range(n): # 정수로 변환
    a[i] = int(a[i])

d = []
for i in range(24): # 인덱스 0 ~ 23까지 생성
    d.append(0)

for i in range(n):
    d[a[i]] = d[a[i]] + 1

for i in range(1, 24):
    print(d[i], end= " ")