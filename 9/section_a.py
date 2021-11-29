w = input()
cnt = 0
while True:
    t = list(map(str, input().split()))
    if t[0] == 'END_OF_TEXT':
        break
    for i in t:
        if w == i.lower():
            cnt += 1
print(cnt)
