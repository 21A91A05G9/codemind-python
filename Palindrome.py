n=int(input())
t=n
s=0
while(n>0):
    d=int(n%10)
    s=s*10+d
    n=n//10
if(s==t):
    print('True')
else:
    print("False")