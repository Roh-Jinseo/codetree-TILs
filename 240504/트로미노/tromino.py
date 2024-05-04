N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

maxi = 0
#block 2*2
for i in range(N-2+1):
    for j in range(M-2+1):
        s1 = arr[i][j+1] + arr[i+1][j]  +arr[i+1][j+1]
        s2 = arr[i][j] + arr[i+1][j]  +arr[i+1][j+1]
        s3 = arr[i][j] + arr[i][j+1]  +arr[i+1][j]
        s4 = arr[i][j] + arr[i][j+1]  +arr[i+1][j+1]
        maxi = max(maxi,s1,s2,s3,s4)
#block1*3
for i in range(N):
    for j in range(M-3+1):
        sub = sum(arr[i][j:j+3])
        maxi = max(maxi, sub)
#transpose
for i in range(N-3+1):
    for j in range(M):
        sub2 = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        # print(sub2)
        maxi = max(maxi,sub2)
 

print(maxi)