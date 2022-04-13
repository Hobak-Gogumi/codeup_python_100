w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

res = w * h * b
res = res / 8
res = res / 1024
res = res / 1024

print("{:.2f} MB".format(res))