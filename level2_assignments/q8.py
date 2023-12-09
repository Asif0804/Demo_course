a = input("Enter the string:")
b = 0

for char in a:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        b += 1

print("Number of vowels:", b)