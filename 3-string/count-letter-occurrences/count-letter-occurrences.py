text = input("Enter a sentence: ")
target_letter = input("Enter the letter to search: ")

count = 0
text = text.lower()

for letter in text:
    if letter == target_letter:
        count += 1

print(f"The letter '{target_letter}' appears {count} times.")
