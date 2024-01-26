lst = []
def avg(x):
    return sum(x)/len(x)

for _ in range(2):
    lst.append(list(map(int, input().split())))
#row avg
print(avg(lst[0]), avg(lst[1]))


lst_t = [list(x) for x in zip(*lst)]
#col avg
col_avg = ''
for col in lst_t:
    col_avg = col_avg + str(avg(col)) + " "
print(col_avg)
#total avg
length = 0
total_sum = 0
for i in lst:
    total_sum = total_sum + sum(i)
    length = length + len(i)
print(total_sum/length)