# 1769 / 3의 배수 / ╰（‵□′）╯

X = list(input())

lint = [int(x) for x in X]
total = sum(lint)

many = 1
while len(str(total)) != 1:
    many += 1
    lint = [int(x) for x in list(str(total))]
    total = sum(lint)

print(many)

if total%3 == 0:
    print("YES")
else:
    print("NO")

# 끝 - ! / o(*^▽^*)┛
