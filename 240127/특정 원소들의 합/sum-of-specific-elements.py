total = 0
count = 1

for _ in range(4):
    nums = list(map(int, input().split()))
    total = total + sum(nums[0:count])
    count += 1

print(total)