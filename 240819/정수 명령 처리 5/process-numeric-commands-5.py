n = int(input())
arr = []
for _ in range(n):
    txt= input().split()
    if txt[0] == "push_back":
        arr.append(txt[1])
    elif txt[0] == "get":
        print(arr[int(txt[1])-1])
    elif txt[0] == "size":
        print(len(arr))
    else: 
        arr.pop()