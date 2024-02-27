N = int(input())
cnt = 0
def f(n):
    global cnt
    if n == 1 :
        print(cnt)
        return
    
    cnt += 1
    if n%2 == 0 : # 짝수
        f(n//2)
    else:
        f(n//3)


f(N)