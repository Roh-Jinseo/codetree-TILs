n = int(input())
def f(n):
    if n <=2 : return n
    return n + f(n-2)
print(f(n))