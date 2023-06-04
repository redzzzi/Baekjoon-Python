# 10871 X보다 작은 수
N, X = map(int,input().split())
pro = list(map(int,input().split()))
less = [k for k in pro if k < X]
print(*less)
