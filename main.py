# Task 1: Variables & Data Types
name = "Precious"
age = 25
height = 5.9
is_student = True
hobbies = ["reading", "coding", "cooking"]

print("Task 1: Variables & Data Types")
print(f"name: {name}, type: {type(name)}")
print(f"age: {age}, type: {type(age)}")
print(f"height: {height}, type: {type(height)}")
print(f"is_student: {is_student}, type: {type(is_student)}")
print(f"hobbies: {hobbies}, type: {type(hobbies)}\n")

# Task 2: User Input & Conditional Statements
print("Task 2: User Input & Conditional Statements")
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
print()

# Task 3: Loops
print("Task 3: For loop - Numbers from 1 to 10")
for number in range(1, 11):
    print(number)

print("\nTask 3: While loop - Even numbers between 1 and 20")
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1
print()

# Task 4: Mini Challenge
print("Task 4: Mini Challenge - Fruits in Uppercase")
fruits = ["apple", "banana", "mango", "grape", "orange"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit.upper())
