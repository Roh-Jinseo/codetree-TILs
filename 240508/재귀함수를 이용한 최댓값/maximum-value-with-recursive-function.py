n =int(input())
arr = list(map(int, input().split()))

def f(n):
    if n == 1 : return arr[0]
    
    
    return max(arr[n-1], f(n-1))
print(f(n))