N = int(input())
arr = list(map(int, input().split()))
mini = int(1e12)
for i in range(N):
    dist = 0
    for j in range(N):
        dist += abs(i-j)*arr[j]
    mini = min(mini, dist)
print(mini)