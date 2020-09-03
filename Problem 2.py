f=1
s=1
b=0
sm=0

while True:
    b=f+s
    f=s
    s=b
    
    if f<= 4000000:
        if f%2 ==0:
            sm+f
    else:
        print(sm)
        break
    