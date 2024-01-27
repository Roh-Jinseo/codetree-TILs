#input
lst = list(map(int, input().split()))

if len(lst) == 0 :
    print()

elif len(lst) == 1:
    print(lst[0])

else:
    n, m = lst    
    a = [
        [ 0 for _ in range(m)]
        for _ in range(n)
    ]

    #
    a[0][0] = 1
    num = 2
    #pt1
    for cross in range(2, min(n, m)):
        row = 0
        col = cross - 1 
        for _ in range(cross):
            a[row][col] = num
            col -= 1
            row += 1
            num += 1
    #pt2
    for col_start in range(min(n, m), max(n, m)):
        cross_len = min(n, m)
        row = 0
        col = col_start - 1
        for _ in range(cross_len):
            a[row][col] = num
            col -= 1
            row += 1
            num += 1
    #pt3
    for cross_len in range(n , 0, -1):
    #    print(n, cross_len)
        row = n - cross_len
        col = m - 1
        
        for _ in range(cross_len):
            a[row][col] = num
    #        print(row, col, a[row][col])
            col -= 1
            row += 1
            num += 1

        

#result
for row in a:
    for i in row:
        print(i, end=" ")
    print()