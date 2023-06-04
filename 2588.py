#곱셈
fst = int(input())
snd = int(input())
print("{}\n{}\n{}\n{}".format(fst*(snd%10),fst*((snd//10)%10),fst*(snd//100),fst*snd))
