# 1, 2, 4, 8, 16, 32, 64, 128, 256

def twopowers(number):
    if number==1:
        return 1
    return 2 * twopowers(number-1)

index=1
while(index<10):
    print(twopowers(index))
    index+=1
