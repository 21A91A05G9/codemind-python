y=int(input())
c=0
for i in range(0,y):
    n=input()
    c=0
    for j in range(0,len(n)):
        x=ord(n[j])-48
        for k in range(0,9):
            if(x==k):
                print("Yes")
                c=1
                break;
        if(c==1):
            break
    else:
        print("No")