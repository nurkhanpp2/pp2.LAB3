n=input()
a=[int(n) for n in n.split()]
for i in a:
    if int(i)%2 == 0:
       print(i, end=' ')