n, m = map(int, input().split())
num = 1
arr = ''
for row in range(n):
    for col in range(m):
        print(num, end=" ")
        num += 1
    print()