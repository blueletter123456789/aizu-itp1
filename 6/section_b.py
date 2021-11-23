n = int(input())
l = [i for i in range(1, 14)]
d = {'S': l.copy(), 'H': l.copy(), 'C': l.copy(), 'D': l.copy()}

for _ in range(n):
    k, v = input().split()
    d[k].remove(int(v))

for key, val in d.items():
    for num in val:
        print(key, num)
