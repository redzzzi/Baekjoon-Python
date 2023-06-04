# 1259 팰린드롬수
ans = []
while True:
    try:
        number = input()
        if number == '0':
            break
        renumber = list(reversed(number))
        chknumber = ''.join(map(str,renumber))
        if number ==chknumber:
            ans.append("yes")
        else: ans.append("no")
    except: break
for i in ans:
    print(i)
