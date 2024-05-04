# import sys; sys.stdin = open("행복수열_input.txt")
"""
4 3
7 1 8 3
6 1 8 7
7 7 7 7
8 1 9 7
"""
N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N) ]

happy = 0
for i in range(N): #가로
    is_happy=False
    for j in range(N-M+1):
        maxi = 0
        cnt = 0
        num = arr[i][j]
        for k in range(M):
            if arr[i][j+k] == num:
                cnt += 1
            else:
                maxi = max(cnt, maxi)
                cnt = 0
            # print(arr[i][j+k],cnt)
        maxi = max(cnt, maxi)
        if maxi >= M :
            happy += 1
            # print((i,j),arr[i][j], maxi,happy)
            break

for i in range(N): #transpose
    for j in range(N):
        if i<j : arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print('---')
# for a in arr:
#     print(a)
for i in range(N): #세로
    for j in range(N-M+1):
        maxi = 0
        cnt = 0
        num = arr[i][j]
        for k in range(M):
            # print((i,j+k), arr[i][j+k],end=" ")
            if arr[i][j+k] == num:
                cnt += 1
            else:
                maxi = max(cnt, maxi)
                cnt = 0
            # print(arr[i][j+k],cnt)
        maxi = max(cnt, maxi)
        if maxi >= M :
            happy += 1
            # print((i,j),arr[i][j], maxi,happy)
            break
        # print()
print(happy)