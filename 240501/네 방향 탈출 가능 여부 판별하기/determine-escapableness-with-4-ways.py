dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(start):
    q=[start]
    visited[start[0]][start[1]]=1

    while q :
        x,y = q.pop(0)
        # x,y = v
        for k in range(4):
            nx = x + dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny))



N, M = map(int, input().split())
arr=[ list(map(int, input().split())) for _ in range(N)]
visited = [ [0]*M for _ in range(N) ]
bfs((0,0))
print(visited[N-1][M-1])