def greet(name):
    print(f"Hello {name}, welcome to Python learning journey!")

user_name = input("Enter your name: ")
greet(user_name)
       
def calculate_square(num):
    return num * num

number = int(input("Enter a number: "))
print(f"The square of {number} is {calculate_square(number)}")
