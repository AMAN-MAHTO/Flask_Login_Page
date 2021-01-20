
while True:
    x=int(input("Enter no: "))
    y=1
    if x==1 or x==0:
        print(1)
    elif x != 0:
        for i in range(2,x+1):
            y*=i
        print(y)
    print()
 
