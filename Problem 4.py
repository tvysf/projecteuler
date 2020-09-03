

p=0



for i in range (101,1000):
    for j in range (101,1000):
        c=i*j
        if str(c) == str(c)[::-1]:
            if c>p:
                p=c

print(p)  