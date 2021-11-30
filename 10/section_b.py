import math
a, b, c = map(float, input().split())
rad = math.radians(int(c))
d = math.sqrt((a**2 + b**2) - (2*a*b*math.cos(rad)))
l = a + b + d
s = math.sqrt(l/2 * (l/2-a) * (l/2-b) * (l/2-d))
h = 2 * s / a
print('{:.8f}'.format(s))
print('{:.8f}'.format(l))
print('{:.8f}'.format(h))
