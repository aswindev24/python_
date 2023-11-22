list=[]
list2=[]
n=int(input("enter the limit and enter the number:"))
for i in range(0,n):
    print("enter the number ",i)
    no=int(input())
    list2.append(no)
    if no>=100:
        no='over'
    list.append(no)
print(list2)
print(list)

