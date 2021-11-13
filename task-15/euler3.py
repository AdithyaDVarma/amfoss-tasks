t=int(input(""))
l=[]
for i in range(t):
    z=int(input(""))
    l.append(z)
for j in l:
    h=int(j)
    i=2
    while i<h:
        if h%i==0:
            h=h/i
        i+=1
    print(h)
