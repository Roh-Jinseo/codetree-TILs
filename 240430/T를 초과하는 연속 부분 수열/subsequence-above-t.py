N, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
maxi = 0
for a in arr:
    if a > t : cnt += 1
    else:
        maxi = max(maxi, cnt)
        cnt = 0
print(maxi)