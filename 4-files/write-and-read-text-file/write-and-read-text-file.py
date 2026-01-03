sentence = input("Enter a sentence: ")

f = open("output.txt", "w")
f.write(sentence)
f.close()

f = open("output.txt", "r")
content = f.read()
print(f"Content in the file: {content}")
f.close()
