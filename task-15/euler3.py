t=int(input(""))
l=[]
for i in range(t):
    z=int(input(""))
    l.append(z)
for j in l:
    i=2
    while i*i < j:
        while j%i==0:
            j=j/i
        i=i+1
    print(int(j))
