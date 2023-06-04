# 10951 A+B-4
ans = []
while True:
    try:
        A, B = map(int,input().split())
        ans.append(A+B)
    except EOFError: break
for i in ans:
    print(i)
