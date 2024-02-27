N = int(input())
cnt = 0
def f(n):
    global cnt
    cnt += 1
    if n == 1 :
        print(cnt)
        return
    
    if n%2 : # 짝수
        # cnt += 1    
        f(n//2)
    else:
        # cnt += 1
        f(n//3)


f(N)