# Count the digits of the Number

def countdigits():
    n = int(input("Enter the Value of n : "))
    dup = n
    cnt = 0
    while(n > 0):
        cnt = cnt + 1
        n = n // 10
    print(f"The Count of the Digits in {dup} is {cnt}.")

countdigits()