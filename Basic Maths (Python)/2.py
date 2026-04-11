# Reverse the Number 

def reversenum():
    n = int(input("Enter the Value of n : "))
    dup = n
    rev = 0
    while(n > 0):
        lastdigit = n % 10
        rev = rev*10 + lastdigit
        n = n // 10
    print(f"The reverse of the {dup} is {rev}.")

reversenum()