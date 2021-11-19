t=int(input(""))
l=[]
for i in range(t):
    p=int(input(""))
    l.append(p)
for i in range(t):
    pall=0
    for j in range(100,l[i]):
        for k in range(100,l[i]):
            pr=j*k
            s1=str(pr)
            if s1==s1[::-1]:
                if pr>pall:
                    pall=pr
    print(pall)
