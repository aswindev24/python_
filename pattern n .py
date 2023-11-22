num=int(input("enter a anumber  "))
x=0
y=0
result=0
for i in range(0,num):
    x=10**i
    y=num*x+y
    result=result+y
    
    print(y)
print(result)
