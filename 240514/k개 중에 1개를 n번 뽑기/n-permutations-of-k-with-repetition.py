K, N = map(int, input().split())
lst = list(range(1, K+1))
path = []
def perm(lev):
    if lev == N :
        print(*path)
        return
    for i in range(K):
        path.append(lst[i])
        perm(lev+1)
        path.pop()
perm(0)