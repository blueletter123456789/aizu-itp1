n = int(input())
ts = hs = 0
for _ in range(n):
    t, h = input().split()
    if t > h:
        ts += 3
    elif t == h:
        ts += 1
        hs += 1
    else:
        hs += 3
print(ts, hs)
