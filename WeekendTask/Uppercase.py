alphabet = input("Enter a string: ")

count = 0

for letter in alphabet:
    if alphabet >= 'A' and alphabet <= 'Z':   
        count = count + 1                 


print("Uppercase letters:", count)
