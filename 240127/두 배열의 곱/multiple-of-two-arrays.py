arr1 = []
arr2 = []


for _ in range(3):
    arr1.append(list(map(int, input().split())))

input()

for _ in range(3):
    arr2.append(list(map(int, input().split())))

for row in range(3):
    for col in range(3):
        print(arr1[row][col] * arr2[row][col], end=" ")
    print()