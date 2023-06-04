# 11021 A+B-7
import sys
num = int(input())
lstsum = []
for _ in range(num):
    lstsum.append(sum(list(map(int,sys.stdin.readline().split()))))
for i in range(0,num):
    print(f"Case #{i+1}: {lstsum[i]}")
