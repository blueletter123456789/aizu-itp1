import statistics
while True:
    n = int(input())
    if n == 0:
        break
    l = list(map(int, input().split()))
    print('{:.8f}'.format(statistics.pstdev(l)))
