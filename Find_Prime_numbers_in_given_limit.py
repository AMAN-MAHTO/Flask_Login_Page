#prime numbers in limit
x=int(input("Enter limit: "))
if x<=1:
    print("There is no Prime number in these limit")
else:
    print("Prime numbers:",end=" ")
    for z in range(2,x+1):
        i=2
        p=True
        while i<z:
            if z%i==0:
                p=False
                break
            i+=1
        if p:
            print(z,end=", ")
        