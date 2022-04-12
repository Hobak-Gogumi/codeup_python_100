h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

res = h * b * c * s
res = res / 8
res = res / 1024
res = res / 1024

print("{:.1f} MB".format(res))