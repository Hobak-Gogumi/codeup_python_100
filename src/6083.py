r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

s = 0

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            s = s + 1

print(s)

# 나는 일일이 더했지만, 합을 r * g * b로 구해도 된다(이게 더 빠른것 같다)