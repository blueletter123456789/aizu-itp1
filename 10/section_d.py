import math
n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))
p1 = p2 = p3 = 0
pi = []
for i in range(n):
    d = abs(x[i]-y[i])
    p1 += d
    p2 += d**2
    p3 += d**3
    pi.append(d)
print('{:.8f}'.format(p1))
print('{:.8f}'.format(math.sqrt(p2)))
print('{:.8f}'.format(p3 ** (1/3)))
print('{:.8f}'.format(max(pi)))
