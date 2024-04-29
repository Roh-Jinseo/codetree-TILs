N = int(input())
cnt = 1
maxi = 1
i = int(input())
pos = True if  i> 0 else False

for _ in range(N-1):
    x = int(input())
    if (x < 0 and pos == False) or (x>0 and pos==True) : #음수, 음수
        cnt += 1
    else :#x > 0 and pos == False : #양수, 음수
        maxi = max(cnt, maxi)
        pos = True if  x> 0 else False
        cnt = 1
maxi = max(cnt, maxi)
print(maxi)