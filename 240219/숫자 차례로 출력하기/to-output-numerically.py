n = int(input())
def print_num(i,n):
    if n < i :
        print()
        return      
    
    print(i, end= " ")
    print_num(i+1, n)
    print(i, end=" ")

print_num(1,n)