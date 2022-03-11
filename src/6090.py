a, m, d, n = input().split()

a = int(a) # 시작 값
m = int(m) # 곱할 값
d = int(d) # 더할 값
n = int(n) # 몇 번째 인지

ans = a

for i in range(2, n + 1):
    ans = (m * ans) + d

print(ans)