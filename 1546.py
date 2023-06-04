# 1546 평균
num = int(input())
scr = list(map(int,input().split()))
bstscr = max(scr)
rescr = []
for i in range(num):
    rescr.append((scr[i]/bstscr)*100)
nwavg = sum(rescr)/num
print(nwavg)
