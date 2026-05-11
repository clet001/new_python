 """ STEPS
1. Collect year
2. use if statement
3. Print answer """

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")

elif year % 100 == 0:
    print("Not a Leap Year")

elif year % 4 == 0:
    print("Leap Year")

else:
    print("Not a Leap Year")
