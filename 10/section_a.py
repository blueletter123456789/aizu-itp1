import math
x1, x2, y1, y2 = map(float, input().split())
x = abs(x1-y1)
y = abs(x2-y2)
print(round(math.sqrt(x**2 + y **2), 8))
