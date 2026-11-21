# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter one more number: "))
print("the qoutient of the numbers that was entered is", number1 / number2)
print("the remainder is", number1 % number2)

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"

animal = input("What is your favorite animal? ")
color = input("What is your favotite color? ")
print("A", color, animal, "would be pretty cool!")

# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).

for even_number in range(0, 11, 2):
    print(even_number)

# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.

pushup_count = int(input("How many pushups can you do?: "))
print("You could do", pushup_count * 7, "pushups in a week!")

# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)

for square_number in range(1, 7):
    print(square_number ** 2)