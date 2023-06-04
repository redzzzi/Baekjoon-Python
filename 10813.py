# 10813 공 바꾸기
N, M = map(int,input().split())
ball = list(range(1,N+1))
for _ in range(M):
    i, j = map(int,input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]
print(*ball)# 10813 공 바꾸기
N, M = map(int,input().split())
ball = list(range(1,N+1))
for _ in range(M):
    i, j = map(int,input().split())
    ball[i-1], ball[j-1] = ball[j-1], ball[i-1]
print(*ball)
