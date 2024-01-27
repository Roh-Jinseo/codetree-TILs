row, col = map(int, input().split())
arr1 = []
arr2 = []
for _ in range(row):
    arr1.append(list(map(int, input().split())))
for _ in range(row):
    arr2.append(list(map(int, input().split())))

for r in range(row):
    ans = ''
    for c in range(col):
        if arr1[r][c] != arr2[r][c] :
            ans = ans + '1' + " "
        else:
            ans = ans + '0' + " "
    print(ans)