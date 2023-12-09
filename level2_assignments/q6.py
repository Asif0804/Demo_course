def power(n):
    if n == 1:
        return True
    elif n < 1 or n % 2 != 0:
        return False
    else:
        return power(n // 2)

n= int(input("Enter a number to check it's a power of two"))
a=power(n)

if a:
    print("Is a power of two", a)
else:
    print("Is not a power of two", a)