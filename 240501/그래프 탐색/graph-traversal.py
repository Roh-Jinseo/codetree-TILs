def dfs(v):
    for w in arr[v]:
        if not visited[w]:
            visited[w] = 1
            path.append(w)
            dfs(w)

N, M = map(int,input().split())
arr = [ [] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
path=[]
visited= [0]*(N+1)
dfs(1)

print(max(0,len(path)-1))