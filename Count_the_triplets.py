for i in range(int(input())):
    n=int(input())
    vk=list(map(int,input().split()))
    a=-1
    for v in range(len(vk)-1):
        for k in range(v+1,len(vk)):
            if vk[v]+vk[k] in vk:
                a+=1
    if a!=-1:
        a+=1
    print(a)