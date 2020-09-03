pf=1

i=2
n=600851475143

while i<=n/i:
    if n % i == 0:
        pf=i
        n=n/i
    else:
        i+=1

if pf<n:
    pf=n
    
print(pf)
    
