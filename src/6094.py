# 두 번째로 풀이했던 방법. for문을 사용하여 최소값 구하기.
n = int(input())
d = input().split()

for i in range(n):
    d[i] = int(d[i])

min = d[0]

for i in range(1, n):
    if(d[i] < min):
        min = d[i]

print(min)

# 처음 풀이했던 방법. 제공되는 min을 이용하여 구함
"""
n = int(input())
d = input().split()

for i in range(n):
    d[i] = int(d[i])

print(min(d))
"""