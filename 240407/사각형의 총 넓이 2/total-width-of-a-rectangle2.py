N = int(input())
arr = [ [0]*200 for _ in range (200) ]
for _ in range(N):
    x1,y1,x2,y2 = map(int, input().split())
    for y in range(y1+100, y2+100):
        for x in range(x1+100, x2+100):
            arr[y][x] = 1
sum_ = 0
for w in arr:
    sum_ += sum(w)
print(sum_)