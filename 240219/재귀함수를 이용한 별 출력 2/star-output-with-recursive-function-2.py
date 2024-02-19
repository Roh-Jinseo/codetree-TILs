n = int(input())
def star(n):
    if n == 0: return # break
    print('* '*n)
    star(n-1)
    print('* '*n)


star(n)