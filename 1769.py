# 2023-11-27 내가 실패했던 문제
# 3의 배수

number = input()
numlist = list(number)
# print(numlist)

count = 0

while int(''.join(numlist)) >= 10:
    renew = 0
    for i in numlist:
        renew += int(i)
        # print(renew)
    numlist = list(str(renew))
    count += 1

def answer(a):
    if a%3==0:
        print("YES")
    else:
        print("NO")
                   
print(count)
answer(int(''.join(numlist)))
