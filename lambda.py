l=int(input("Enter the length of rectangle " ))
b=int(input("Enter the breadth of rectangle " ))
x=lambda l,b : l*b
print("Area of rectangle : ",x(l,b))

a=int(input("Enter the side of squre " ))
x=lambda a:a*a
print("Area of squre: ",x(a))

s=int(input("Enter the breadth of triangle :"))
p=int(input("Enter the height of rectangle : "))
x=lambda s,p: 0.5*s*p
print("Area of triangle is : ",x(s,p))


