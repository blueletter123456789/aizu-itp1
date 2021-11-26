r, c = map(int, input().split())
s = []
for _ in range(r):
    l = list(map(int, input().split()))
    l.append(sum(l))
    print(' '.join(list(map(str, l))))
    s.append(l)
l2 = list()
for i in range(c+1):
    l2.append(sum([s[j][i] for j in range(r)]))
print(' '.join(list(map(str, l2))))
