n = int(input(""))
m = input("").split()
m = list(map(int,m))
m.sort()
l = list(set(m))
a = []
for i in l:
    z=m.count(i)
    a.append(z)
o=len(a)
print(str(a[o-2]) + " " + str(len(a)))
