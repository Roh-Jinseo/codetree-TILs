N = int(input())
sum_ = 0
def f(n):
    global sum_
    if n == 0 : 
        print(sum_)
        return

    sum_ += n
    f(n-1)

f(N)