a=int(input())
c=0
t=a
x=a
s=0
while(a!=0):
    r=a%10
    c+=1
    a=a//10
while(t!=0):
    r1=t%10
    s=s+(r1**c)
    c-=1
    t=t//10
if(s==x):
    print("True")
else:
    print("False")