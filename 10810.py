# 10810 공 넣기
N, M = map(int,input().split())
ball = [0]*N
for _ in range(M):
    st, end, num = map(int,input().split())
    if st == end:
        ball[st-1] = num
    else:
        for i in range(st-1,end):
            ball[i] = num
print(*ball)
