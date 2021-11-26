while True:
    n, x = map(int, input().split())
    a = 0
    if n == 0 and x == 0:
        break
    elif (n-1)*3 >= x:
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                s = x - (i + j)
                if j < s <= x and s <= n:
                    a += 1
    print(a)
