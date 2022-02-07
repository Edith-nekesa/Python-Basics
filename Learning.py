# to comment multiple lines select lines and ctrl+/
# Conditional statements if,elif,else

temperature = int(input("Enter Temperature: "))

if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's noice")
print("Done")

# ternary operations: combined/shrtened form of condition statements

age = int(input("Enter age: "))
message = "Eligible" if age >= 18 else "Not eligible"
print(message)
# this is how we would have written it as a condition statement
# if age >= 18:
#   message = "Eligible"
# else:
#   message = "Not eligible"

# Logical Operators: AND, OR, NOT
# AND both operators need to be true to fulfil the condition
# OR at least on to be true

high_income = False
good_credit = False
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")

# python condition operators are short circuit, when using AND if the first condition met is false it automatically stops and the rest of the conditions are not evaluated. OR when it reaches a condition that is true it stops.
# Chaining comparison operators
# age should be between 18 and 65
age2 = 22
# chaining
if 18 <= age2 < 65:
    print("Eligible")
# if age >=18 and age < 65:  (the initial statement)

# we use loops to create repetition

# FOR LOOPS
# -->(number of times argument to be passed):  always end with colon like if statement
# number is a variable of type int
# range()generates the immutable(cannot change) sequence of numbers starting from the given start integer to the stop integer.
# there are three types: range(stop), range(start, stop), range(start, stop, step).
for number in range(3):
    # --> statement that should be repeated.
    print("Attempt", number + 1, (number + 1) * ("."))
# can also pass the argument range as:
# for number in range(1, 4)
# print("Attempt", number + (".")) ...or
for number in range(1, 10, 2):  # passing 2 as a step
    print("Attempt", number * ("."))

# FOR ELSE

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# NESTED LOOPS -->putting a loop inside another loop
for x in range(5):  # Outer Loop
    for y in range(3):  # Inner Loop
        # formatted strings can also write: print(f"x:{x}, y:{y}")
        print(f" ({x},{y})")


# just a note:
# 	for loop -	Is an iterator based loop, which steps through the items of iterable objects like lists, tuples, string and executes a piece of code repeatedly for a number of times, based on the number of items in that iterable object.
#  	while loop - Executes a block of statements repeatedly as long as the condition is TRUE.
