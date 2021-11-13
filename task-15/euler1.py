n=int(input(""))
l=[]
s=0
for i in range(n):
    m=int(input(""))
    l.append(m)
for i in range(n):
    z=l[i]
    for j in range(1,z):
        if j%3==0 or j%5==0:
            s=s+j
    print(s)
    s=0
