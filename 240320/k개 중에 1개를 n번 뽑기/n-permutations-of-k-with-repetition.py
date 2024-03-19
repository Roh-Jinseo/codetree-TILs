def perm(lev):
    if lev == M :
        print(*path)
        return
    
    for i in range(N):
        path.append(arr[i])
        perm(lev+1)
        path.pop()

N, M = map(int, input().split())
arr = list(range(1, N+1))
path=[]

perm(0)