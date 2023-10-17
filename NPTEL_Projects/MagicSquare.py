def magic_sq(n):
    ans=n*((n*n)+1)//2
    print(ans)
    magic=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magic.append(l)
    i=n//2
    j=n-1
    
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1
        if(magic[i][j]!=0):
            i+=1
            j-=2
            continue
        else:
            magic[i][j]=count
            count+=1
        i-=1
        j+=1
    for i in range(n):
        for j in range(n):
            print(magic[i][j],end=' ')
        print()
magic_sq(11)