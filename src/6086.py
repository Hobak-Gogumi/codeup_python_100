n = int(input())

s = 0
i = 1

while True:
    s = s + i

    if s >= n:
        break

    i = i + 1

print(s)