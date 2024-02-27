N = int(input())
s = 0
def f(n):
    global s
    if n <=0:
        print(s)
        return
    s += n
    f(n-2)

f(N)