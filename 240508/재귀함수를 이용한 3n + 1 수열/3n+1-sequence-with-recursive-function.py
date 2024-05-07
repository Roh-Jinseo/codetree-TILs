n = int(input())
cnt = 0
def f(n):
    global cnt
    if n == 1 : return 
    cnt += 1
    if n%2==0:
        return f(n//2)
    else:
        return f(n*3+1)
f(n)
print(cnt)