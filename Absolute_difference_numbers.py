n,m=map(int,input().split())
l=n
a=0
while(n):
    n//=10
    a+=1
n=l
b=pow(10,m)
c=pow(10,a-m)
v=n%b
k=n//c
print(abs(v-k))