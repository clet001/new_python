"""STEPS
1. collect inputs(Three scores) using floats
2. Divide the scores by 3 to get the avearge
3. Compare scores using conditional staements
4. print """



first_score = float(input("Enter first score: "))
second_score = float(input("Enter second score: "))
third_score = float(input("Enter third score: "))

average_score = (first_score + second_score + third_score) / 3

print("Average Score is", average_score)


if average_score >= 90:
    print("Grade = A")

elif average_score >= 80:
    print("Grade = B")

elif average_score >= 70:
    print("Grade = C")

elif average_score >= 60:
    print("Grade = D")

else:
    print("Grade = F")

