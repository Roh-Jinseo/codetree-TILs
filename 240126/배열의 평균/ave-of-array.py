lst = []
def avg(x):
    return sum(x)/len(x)

for _ in range(2):
    lst.append(list(map(int, input().split())))
#row avg
print(round(avg(lst[0]),1), round(avg(lst[1]),1))


lst_t = [list(x) for x in zip(*lst)]
#col avg
col_avg = ''
for col in lst_t:
    col_avg = col_avg + str(round(avg(col),1)) + " "
print(col_avg)
#total avg
length = 0
total_sum = 0
for i in lst:
    total_sum = total_sum + sum(i)
    length = length + len(i)
print(round(total_sum/length, 1))