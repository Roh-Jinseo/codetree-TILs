n = int(input())
start = 1
end = n + 1
arr = []
for i in range(n):
    arr.append( list(range(start, end)) )
    start = end
    end = end + n

result = map(list, zip(*arr))


for row in result:
    for elem in row:
        print(elem, end=" ")
    print()