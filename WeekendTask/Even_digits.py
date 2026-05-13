num = input("Enter a number: ")

sum_even = 0
digit = 0

for digit in num:
    
    if digit % 2 == 0:
    sum_even = sum_even + digit

print("sum even digits is", sum_even)
