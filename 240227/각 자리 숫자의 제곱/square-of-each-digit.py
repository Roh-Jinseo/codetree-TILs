N = int(input())

total = 0
def f(n):
    global total
    if n == 0 :
        print(total) 
        return
    
    total += (n%10)**2
    f(n//10)


f(N)