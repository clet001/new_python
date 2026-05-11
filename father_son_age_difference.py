"""STEPS
1. Collect input from user(Father and Son current age)
2. Subtract Father's age from son's age
3. Multiply the result by 2
4. Print Result """


father_age = int(input("Enter father's age: "))
son_age = int(input("Enter son's age: "))

difference = father_age - son_age

father_age_x_year = difference * 2

print("Result:", father_age_x_year)
