n = int(input())
num = 1
arr = [ 
    [ 0 for _ in range(n)] 
    for _ in range(n) 
    ]
for row in range(n):
    for col in range(n):
        arr[col][row] = num
        num += 1

#출력
for ar in ar :
    for i in ar :
        print(i, end = " ")
    print()