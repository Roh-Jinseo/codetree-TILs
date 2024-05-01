"""
4 5
1 2 4 7 5
4 2 5 5 2
5 7 3 2 6
6 7 4 5 1

//
4 4
"""
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(v):
    global cnt
    x,y = v
    for idx in range(4):
        nx=x+dx[idx]
        ny=y+dy[idx]
        if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and safehome[nx][ny]:
            cnt += 1
            visited[nx][ny] = 1
            dfs((nx,ny))

def flood_check(k):
    for i in range(N):
        for j in range(M):
            if arr[i][j] > k : safehome[i][j] = 1

N, M= map(int,input().split())
arr=[ list(map(int, input().split())) for _ in range(N) ]
safe=[]
max_height = 0
for ar in arr:
    max_height = max(max_height, max(ar))

for k in range(1, max_height+1):
    visited=[ [0]*M for _ in range(N) ]
    ans = []
    safehome = [ [0]*M for _ in range(N) ]
    flood_check(k)
    for i in range(N):
        for j in range(M):
            cnt = 0
            if not visited[i][j] and safehome[i][j] :
                cnt+=1
                visited[i][j] = 1
                dfs((i,j))
                if cnt > 0 : ans.append(cnt)
    # print(k,ans)
    # for v in visited:
    #     print(v)
    safe.append((len(ans),k))
safe.sort(key=lambda x: (-x[0],x[1]))
print(*safe[0])