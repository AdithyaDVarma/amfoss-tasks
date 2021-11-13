t=int(input(""))
l=[]
for i in range(t):
    p=int(input(""))
    l.append(p)
for i in range (t):
    for j in range(1,l[i]):
        a=0
        b=1
        sum=0
        while b<j:
            if b%2==0:
                sum+=b
            a,b=b,a+b
    print(sum)

