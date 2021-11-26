while True:
    a = input()
    if a == '0':
        break
    s = 0
    for i in a:
        s += int(i)
    print(s)
