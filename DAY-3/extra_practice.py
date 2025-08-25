# Day-3 Extra Practice

# 1. Sum of Digits
number = int(input("Enter a number: "))
total = 0
while number > 0:
    digit = number % 10
    total += digit
    number //= 10
print("Sum of digits:", total)

# 2. Reverse a String
string = input("Enter a string: ")
print("Reversed string:", string[::-1])

# 3. Word Frequency Count
sentence = input("Enter a sentence: ")
words = sentence.split()
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("Word frequency:", frequency)

# 4. Palindrome Checker
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome.")

# 5. Find Missing Number in List
numbers = [1, 2, 3, 5]  # Example list
n = 5
expected_sum = (n * (n + 1)) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum
print("Missing number is:", missing_number)
