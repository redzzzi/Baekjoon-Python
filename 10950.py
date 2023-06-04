# 10950 A+B-3
num = int(input())
sum = []
for _ in range(num):
    A, B = map(int,input().split())
    sum.append(A+B)
for j in sum:
    print(j)
