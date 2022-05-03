n=int(input())
s=0
while(n>0):
    d=int(n%10)
    if(d>s):
        s=d
    n=n//10
print(s)