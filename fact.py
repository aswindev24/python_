def fact(x):
    if x==1:
        return 1
    else:
        a=(x*fact(x-1))
        return a
num=int(input("Enter a number"))
answ=fact(num)
print(answ)
