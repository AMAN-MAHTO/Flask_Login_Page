def perfect_num(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f"{n} is a Perfect number")
    else:
        print(f"{n} is not a Perfect number")

perfect_num(int(input("Enter number: ")))
