N = int(input())
cnt = 0

def perm(cursum):
    global cnt
    if cursum == N :   
        cnt += 1
        return
    if cursum > N :
        return
    
    for i in range(1, 5):
        perm(cursum + i)

perm(0)
print(cnt)