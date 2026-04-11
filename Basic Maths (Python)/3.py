# Check Palindrome Number

def palindrome():
    n = int(input("Enter the Value of n : "))
    dup = n
    rev = 0
    while(n > 0):
        lastdigit = n % 10
        rev = rev * 10 + lastdigit
        n = n // 10
    if dup == rev:
        print("Palindrome Number")
    else:
        print("Not Palindrome")
    

palindrome()