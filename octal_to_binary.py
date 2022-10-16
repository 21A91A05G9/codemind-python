def bin(s):
    k=''
    while(s>0):
        r=s%2
        s=s//2
        k+=str(r)
    return k[::-1]
n=int(input())
c=s=0
while n:
    r=n%10
    s+=r*pow(8,c)
    c+=1
    n=n//10
print(bin(s))