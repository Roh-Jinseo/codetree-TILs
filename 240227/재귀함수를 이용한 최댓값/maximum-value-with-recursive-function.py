N = int(input())
arr = list(map(int, input().split()))
maxi = 0
def f(n):
    global maxi
    if n == N : 
        return

    if maxi < arr[n]:
        maxi = arr[n]    
    f(n+1)
f(0)
print(maxi)