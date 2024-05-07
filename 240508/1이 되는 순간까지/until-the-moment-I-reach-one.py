n = int(input())

def f(n):
    if n==1:
        return 0
    if n%2: #홀수
        return 1 + f(n//3)
    else:
        return 1 + f(n//2)
print(f(n))