def fib(n):   # n is the limit of fibonacci series
    a=0    
    b=1    
    c=1
    print(f"Fibonacci series")
    print(a,end=", ")
    while c<=n:
        print(c,end=", ")
        c=a+b 
        a=b 
        b=c

fib(int(input("Enter limit: ")))