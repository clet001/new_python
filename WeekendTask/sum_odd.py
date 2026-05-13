num = input("Enter a number: ")

sum_odd = 0
digit = 0
for digit in num:
    
    if digit % 2 != 0:
        sum_odd = sum_odd + digit

print("Sum of odd number =", sum_odd)
