# speed of getting factor is depend upon how much greater prime no while come during factorization



def loop():
    while True:
        x = int(input("Enter no: "))
        y = 2
        print ('Factors are:')
        while x > 1:
            if x % y == 0:
                print(y)
                x = x / y
                continue
            
            if x == 0:
                break
            if y>x/2:
                print(int(x))
                break
            else:
                y+=1
        

    
print('WELLCOM TO FACTOR COAD')
loop()




