n=int(input())
l=list(map(int,input().split()))
d=max(l)
while(d):
   c=0
   for i in l:
       if(d%i==0):
           c+=1
   if(c==len(l)):
        print(d)
        break
   d+=1