num = int(input("Enter number: "))
x = num  
sum = 0

while x > 0:
    a = x % 10  # e.g: x=153 then a=3
    sum += (a**3)
    # e.g: x=153 then x/10= 15.3 but\
    # due to convertion into int x=15
    x = int(x/10)    
                    
if sum == num:
    print(f'{num} is an Armstrong number ')
else:
    print(f'{num} is not an Armstrong number ')
