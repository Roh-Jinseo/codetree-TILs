a, b, c = map(int, input().split())
total = 0
def f(n):
    global total
    if n <= 0:

        return

    total += n % 10
    f(n//10)    

f(a*b*c)
print(total)