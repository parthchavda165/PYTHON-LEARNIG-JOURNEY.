"""
Day 5: Escape Sequences in Python
---------------------------------
This file demonstrates the usage of different escape sequences in Python strings.
"""

# \n - New line
print("Hello\nWorld")  # Output: Hello (newline) World

# \t - Tab space
print("Hello\tWorld")  # Output: Hello   World

# \\ - Backslash
print("This is a backslash: \\")

# \" and \' - Quotes inside string
print("He said, \"Python is awesome!\"")
print('It\'s a beautiful day!')

# \b - Backspace
print("Hello\bWorld")  # Removes previous character

# \r - Carriage return (moves cursor to start)
print("12345\rABCDE")  # Output: ABCDE

# \f - Form feed (rarely used, acts like new line in console)
print("Hello\fWorld")
