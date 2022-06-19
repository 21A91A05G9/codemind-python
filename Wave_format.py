def fun(a):
    return max(a)
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    if(i%2==1):
        x=fun(a)
        a.remove(x)
        y=fun(a)
        print(y,end=' ')
        print(x,end=' ')
        a.remove(y)
for i in a:
   print(i)