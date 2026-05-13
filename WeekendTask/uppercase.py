alphabet = input("Enter a string: ")

count = 0

for letter in alphabet:

    if alphabet >= 'a' and alphabet <= 'z':
        count += 1

print("Lowercase letters:", count)
