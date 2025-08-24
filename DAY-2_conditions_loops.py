# Day 2 - Python Conditions and Loops

# Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Print numbers from 1 to 10 using loop
print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# While loop example
count = 1
print("\nWhile Loop Counting:")
while count <= 5:
    print(f"Count: {count}")
    count += 1
