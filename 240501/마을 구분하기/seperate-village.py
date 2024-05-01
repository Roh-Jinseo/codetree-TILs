"""
5
0 1 0 0 1
0 1 0 1 1
0 1 0 0 1
0 1 1 1 1
1 0 0 0 0

//
2
1
11
"""
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(v):
    global cnt
    x,y = v
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny]:
            cnt += 1
            visited[nx][ny] = 1
            dfs((nx,ny))


N=int(input())
arr=[ list(map(int, input().split())) for _ in range(N) ]
visited=[ [0]*N for _ in range(N) ]
ans = []
for i in range(N):
    for j in range(N):
        cnt = 1
        if not visited[i][j] and arr[i][j] :
            visited[i][j] = 1
            dfs((i,j))
            if cnt > 0 : ans.append(cnt)
# print(visited)
print(len(ans))
ans.sort()
for a in ans:
    print(a)