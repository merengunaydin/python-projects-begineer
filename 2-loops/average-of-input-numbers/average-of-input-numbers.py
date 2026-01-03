count = int(input("How many numbers will you enter? "))

total = 0

for i in range(count):
    number = int(input(f"Enter number {i+1}: "))
    total += number

print(f"Average: {total / count}")
