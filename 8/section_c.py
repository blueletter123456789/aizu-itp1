d = {k: 0 for k in [chr(ord("a")+i) for i in range(26)]}
while True:
    try:
        s = input().lower()
        for c in s:
            if c in d.keys():
                d[c] += 1
    except EOFError:
        break
for k, v in d.items():
    print(f'{k} : {v}')
