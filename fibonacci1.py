def getFibNumber(number):
    if number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return getFibNumber(number-1) + getFibNumber(number-2)
a=getFibNumber(30)
print(a)