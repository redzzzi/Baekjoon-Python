total = int(input())
num = int(input())
    
totalchk = 0

for _ in range(num):
    a, b = map(int, input().split())
    totalchk += a*b

if total == totalchk:
    print("Yes")
else: print("No")
