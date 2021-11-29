while True:
    n = input()
    if n == '-':
        break
    m = int(input())
    for _ in range(m):
        h = int(input())
        n = n[h:] + n[:h]
    print(n)
