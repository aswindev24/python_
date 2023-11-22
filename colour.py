colour=input("enter the colours with coma sperated")

print("old colour are :",colour)
newcolour=colour.split(",")
x=len(newcolour)
print("new colours are:",newcolour[0],newcolour[x-1])
