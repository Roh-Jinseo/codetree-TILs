brackets = list(input())
cnt = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        for j in range(i, len(brackets)):
            if brackets[j] == ')':
                cnt += 1
print(cnt)