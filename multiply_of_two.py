def multiply(a,b):
    if a<b:
        return multiply(b,a)
    elif b!=0:
        return a+multiply(a,b-1)
    else:
        return 0
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
z=multiply(a,b)
print(z)
