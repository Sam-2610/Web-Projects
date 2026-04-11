# Check the Armnstrong Number

def armstrong():
    n = int(input("Enter the Value of n : "))
    armst = 0
    dup = n
    while(n > 0):
        lastdigit = n % 10
        armst = armst + (lastdigit)**3
        n = n // 10
    if dup == armst:
        print("Armstrong Number")
    else:
        print("Not Armstrong")

armstrong()
    