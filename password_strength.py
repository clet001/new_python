""" STEPS
1. collect password
2. Check lenght using len
3 use if statements
4. print """

user_password = input("Enter password: ")

length = len(user_password)




if length <= 10:
    print("Medium")
elif length <= 6:
    print("Weak")
elif length <=1:
    print("Invalid")
