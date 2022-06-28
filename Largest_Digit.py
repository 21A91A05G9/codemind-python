n=int(input())
a=[]
while(n):
    a.append(n%10)
    n//=10
print(max(a))