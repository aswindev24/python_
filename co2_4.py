for i in range(1000,10000,1):
    for j in range(32,100):
        i==j*j
        st=str(i)
        if int((st[0]%2==0) and int(st[1]%2==0) and int(st[2]%2==0) and int(st[3]%2==0)):
            print(i)

    
