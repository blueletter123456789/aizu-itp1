s = list(input())
q = int(input())
for _ in range(q):
    l = list(input().split())
    if l[0] == 'print':
        print(''.join(s[int(l[1]):int(l[2])+1]))
    elif l[0] == 'reverse':
        s[int(l[1]): int(l[2])+1] = [s[i] for i in range(int(l[2]), int(l[1])-1, -1)]
    else:
        s[int(l[1]): int(l[2])+1] = l[3]
