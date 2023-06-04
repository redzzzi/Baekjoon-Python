# 11022 A+B-8
import sys
num = int(input())
script = []
for i in range(num):
    A, B = map(int,sys.stdin.readline().split())
    script.append(f"Case #{i+1}: {A} + {B} = {A+B}")
for j in script:
    print(j)
