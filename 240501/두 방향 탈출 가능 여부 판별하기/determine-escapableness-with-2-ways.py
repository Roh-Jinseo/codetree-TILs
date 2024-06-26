dx = [0, 1]
dy = [1, 0]


def dfs(v):
    global flag
    if flag :
        return
    x, y = v
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[x][y]:
            visited[nx][ny] = 1
            if nx == N - 1 and ny == M - 1:
                # print("goal")
                flag=True
                return 1
            dfs((nx, ny))

    return 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
end = (N - 1, M - 1)
path = []
visited = [[0] * M for _ in range(N)]
visited[0][0]=1
flag=False
dfs((0, 0))
print(int(flag))
# print(visited)