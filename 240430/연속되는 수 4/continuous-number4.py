N = int(input())
i = int(input())
cnt = 1
maxi = 1
for _ in range(N-1):
    x = int(input())
    if i < x :
        cnt += 1
    else:
        maxi = max(cnt, maxi)
        cnt = 1
    i = x
maxi = max(cnt, maxi)
print(maxi)