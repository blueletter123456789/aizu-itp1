n, m, l = map(int, input().split())
c = []
a = []
b = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    b.append(list(map(int, input().split())))

for j in range(n):
    tmp = []
    for k in range(l):
        g = 0
        for i in range(m):
            g += a[j][i] * b[i][k]
        tmp.append(g)
    print(' '.join(list(map(str, tmp))))
