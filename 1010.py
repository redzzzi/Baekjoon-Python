# 1010 다리 놓기

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return(result)

def combination(n,r):
    result = factorial(n)/(factorial(r)*factorial(n-r))
    return(result)

T = int(input())

num_case = []

for _ in range(T):
    N, M = map(int,input().split())
    num = combination(M,N)
    num_case.append(num)

for j in num_case:
    print(int(j))

# (ノ｀Д)ノ
