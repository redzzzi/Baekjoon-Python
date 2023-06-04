word = str(input())

relst = reversed(list(word))

reword = ''.join(map(str,relst))


if word == reword:
    print(1)
else: print(0)
