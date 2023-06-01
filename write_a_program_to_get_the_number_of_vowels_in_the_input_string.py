n=input()
c=0
a=n.lower()
for i in a:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c+=1
print("%d"%(c))