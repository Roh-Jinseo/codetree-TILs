arr = [ [0]*2000 for _ in range(2000)]
for _ in range(2):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1+1000,y2+1000):
        for x in range(x1+1000, x2+1000):
            arr[y][x] = 1

x1,y1,x2,y2 = map(int, input().split())
for y in range(y1+1000,y2+1000):
    for x in range(x1+1000, x2+1000):
        arr[y][x] = 0

ans = 0
for a in arr:
    ans += sum(a)
print(ans)