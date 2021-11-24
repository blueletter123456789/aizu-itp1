n = int(input())
d = [[['0' for _ in range(10)] for _ in range(3)] for _ in range(4)]
for _ in range(n):
    b, f, r, v = map(int, input().split())
    d[b-1][f-1][r-1] = str(int(d[b-1][f-1][r-1]) + v)
for b in range(len(d)):
    for f in d[b]:
        s=' '.join(f)
        print(" {}".format(s))
    if b != 3:
        print('#'*20)
