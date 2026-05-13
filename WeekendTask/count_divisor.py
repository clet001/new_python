
number = int(input("Enter a number: "))

count = 0                     


for count in range(1, number):
    if number % count == 0:
        print(count)              
        count += 1            

print("divisors =", count)
