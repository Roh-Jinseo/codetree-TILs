dx=[[-2,-1,1,2],[-1,0,1,0],[-1,1,1,-1]]
dy=[[0,0,0,0],[0,1,0,-1],[1,1,-1,-1]]
def dfs(lev):
    global maxi

    if lev == len(bombs):
        cnt = 0
        for r in range(N):
            for c in range(N):
                if arr[r][c] :
                    cnt += 1
        maxi = max(cnt,maxi)
        return

    x,y=bombs[lev]
    for k in range(3):
        for l in range(4):
            nx=x+dx[k][l]
            ny=y+dy[k][l]
            if 0<=nx<N and 0<=ny<N :
                arr[nx][ny] += 1
        dfs(lev+1)
        for l in range(4):
            nx=x+dx[k][l]
            ny=y+dy[k][l]
            if 0<=nx<N and 0<=ny<N :
                arr[nx][ny] -= 1
            
        
        
            


N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
maxi = 0
bombs = []
for i in range(N):
    for j in range(N):
        if arr[i][j] : bombs.append((i,j))

dfs(0)
print(maxi)