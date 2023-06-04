# 4096 팰린드로미터

while True:
    num = input()
    if num == "0":
        break
    else:
        if num == num[::-1]:
            print(0)
        else:
            length = len(num)
            distance = 0
            while num != num[::-1]:
                distance += 1
                plus = str(int(num)+1)
                i = 0
                while length != len(plus+"0"*i):
                    i += 1
                num = "0"*i + str(int(num)+1)
            print(distance)
