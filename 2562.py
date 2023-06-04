# 2562 최댓값
lstnum = []
for _ in range(9):
    num = int(input())
    lstnum.append(num)
maximum = max(lstnum)
order = lstnum.index(maximum) + 1
print("{}\n{}".format(maximum, order))
