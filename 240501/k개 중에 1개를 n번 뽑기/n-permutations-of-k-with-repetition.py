def dfs(lev):
    if lev == N:
        print(*path)
        return
    for i in range(1, K+1):
        path.append(i)
        dfs(lev+1)
        path.pop()


K, N = map(int,input().split())
path = []
dfs(0)