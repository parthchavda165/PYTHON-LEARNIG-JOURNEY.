"""
Day 5: print() Function Parameters in Python
--------------------------------------------
This file demonstrates different parameters of the print() function:
- sep
- end
- file
- flush
"""

# sep parameter: separates values with given string
print("Python", "Java", "C++", sep=" | ")

# end parameter: controls what is printed at the end
print("Hello", end=" ")
print("World")  # Output: Hello World

# file parameter: send output to a file or stream
import sys
print("This message goes to the console", file=sys.stdout)

# flush parameter: immediately flush the output buffer
import time
print("Loading...", end="", flush=True)
time.sleep(1)
print("\rDone!")  # \r moves cursor back to the start
