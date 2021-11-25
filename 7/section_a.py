while True:
    m, f, r = map(int, input().split())
    if (m + f + r) == -3:
        break
    if m != -1 and f != -1:
        a = m + f
        if a >= 80:
            print('A')
        elif a >= 65:
            print('B')
        elif a >= 50:
            print('C')
        elif a >= 30:
            if r >= 50:
                print('C')
            else:
                print('D')
        else:
            print('F')
    else:
        print('F')
