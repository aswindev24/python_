a=[]
b=[]
add=0
limit1=int(input("Enter the limit of 1st"))
limit2=int(input("Enter the 2nd limt"))
for i in range(0,limit1):
    print("enter the first list numbers:",i+1)
    no=int(input())
    a.append(no)
    add=add+a[i]
print("the first list elements are",a)
print("sum",add)
length1=len(a)
print("the length of 1st ",length1)
for j in range(0,limit2):
    print("enter the 2nd numbers",j+1)
    no=int(input())
    b.append(no)
    add=add+b[j]
print("the second list elements are:",b)
print("sum",add)
length2=len(b)
print("the lenth of 2nd list ",length2)
if length1 == length2:
    print("both are of same length")
else:
    print("both are diffrent size")
