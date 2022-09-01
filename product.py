def product (n):
    if n==1:
        return 1
    else:
        return (n*product(n-1))
n=int(input("enter any num.:"))
z=product(n)
print(z)