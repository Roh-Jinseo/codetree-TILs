def dfs(cursum):
    global cnt
    if cursum == N :
        cnt += 1
        return
    elif cursum > N:
        return            
    for num in nums:
        dfs(cursum+num)


N = int(input())
nums=[1,2,3,4]
cnt = 0
dfs(0)
print(cnt)