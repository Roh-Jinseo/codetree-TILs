n, m = map(int, input().split())
num = 0

arr = [
    [ 0 for _ in range(m)]
    for _ in range(n)
]

for col in range(m):
    for row in range(n):
        if col % 2 == 0 : # 짝수
            arr[row][col] = num
        else: #홀수
            arr[n - row - 1][col] = num
        num += 1

#출력
for row in arr:
    for val in row:
        print(val, end = " ")
    print()