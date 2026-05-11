weight = float(input("Enter Weight in Kg:"))
height = float (input("Enter height in meters:"))

bmi = (weight / height)*2

if bmi > 18.5:
    print("Underweight")

if bmi >= 25.5:
    print("Normal")

if bmi >= 29.5:
    print("Overweight")

else
    print("Obese")
