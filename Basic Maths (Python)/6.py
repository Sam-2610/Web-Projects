def Prime():
    n = int(input("Enter the value of n: "))
    cnt = 0

    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1

    if cnt == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

Prime()