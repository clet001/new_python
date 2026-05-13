sentence = input("Enter a sentence: ")

count = 1   

for letter in sentence:
    if letter == ' ':
        count += 1

print("total numb of words =", count)
