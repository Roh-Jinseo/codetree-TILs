N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)]
maxi = 0
for r in range(N-3+1):
    for c in range(N-3+1):
        cnt = 0
        for k in range(3):
            cnt += arr[r+k][c:c+3].count(1)
        maxi = max(maxi,cnt)
print(maxi)