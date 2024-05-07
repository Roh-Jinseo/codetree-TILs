a,b,c = map(int, input().split())
x=a*b*c
def f(n):
    return 0 if n == 0  else n%10 + f(n//10)
print(f(x))