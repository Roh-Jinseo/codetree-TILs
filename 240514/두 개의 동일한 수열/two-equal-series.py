n = int(input())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print('Yes') if sorted(l1)==sorted(l2) else print('No')