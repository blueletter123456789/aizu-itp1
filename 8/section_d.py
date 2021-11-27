s = input()
p = input()
s *= (100 // len(s)) + 2
if p in s:
    print('Yes')
else:
    print('No')
