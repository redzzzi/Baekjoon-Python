# 15552 빠른 A+B
import sys
num = int(input())
ans = []
for _ in range(num):
    case = map(int,sys.stdin.readline().split())
    ans.append(sum(case))
for j in ans:
    print(j)
