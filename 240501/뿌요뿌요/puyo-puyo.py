"""
3
1 1 1
2 1 2
1 1 1

"""
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def dfs(v):
    global cnt
    x,y = v
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny]==arr[x][y]:
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
        if not visited[i][j]  :
            visited[i][j] = 1
            dfs((i,j))
            ans.append(cnt)
# 블럭 수, 최대길이
blocks = 0
for a in ans:
    if a>=4: blocks+=1
print(blocks, max(ans))