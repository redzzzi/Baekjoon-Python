# 10952 A+B-5
ans = []
while True:
    try:
        A, B = map(int,input().split())
        if A == 0 and B == 0:
            break
        ans.append(A+B)
    except: break
for i in ans:
    print(i)
