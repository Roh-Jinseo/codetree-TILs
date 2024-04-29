N = int(input())
i = int(input())
maxi = 1
cnt = 1
for _ in range(N-1):
    j = int(input())
    if i == j : cnt += 1
    else:
        maxi = max(cnt, maxi)
        cnt = 1
        i = j
maxi = max(cnt, maxi)
print(maxi)