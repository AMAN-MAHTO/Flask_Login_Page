
def loop():
    x= int(input('Enter no :'))
    for i in range(2,x):
        if x%i!=0:
            print('{} is a Prime no'.format(x))
        else:
            print('{} is not a Prime no'.format(x))
        y = int(input('For quit enter "0"='))
        if y == 0:
            quit()
        loop()
print ("WELLCOME" )
print("Enter no to know its a prime no")
y = 1
if y == 0:
    quit()

loop()


