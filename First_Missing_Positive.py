n=int(input())
v=list(map(int,input().split()))
k=[]
for i in v:
    if i>=0:
        k.append(i)
k.sort()
for i in range(1,max(k)+2):
    if i not in k:
        print(i)
        break