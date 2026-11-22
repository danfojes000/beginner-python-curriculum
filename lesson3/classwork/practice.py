# Problem 1
# Ask the user to enter their height in centimeters.
# Print "Tall" if the height is greater than 170, otherwise print "Short".

height = int(input("How tall are you in centimeters? "))
if height > 170:
    print("Tall")
else:
    print("Short")

print("Height determination complete.")

# Problem 2
# Ask the user for their age.
# If they are 18 or older, print "Adult", else print "Minor".

age = int(input("How old are you? "))
if height > 18:
    print("Adult")
else:
    print("Minor")

print("Age determination complete.")

# Problem 3
# Ask the user to enter a number.
# Print "Fizz" if it is divisible by 3, "Buzz" if divisible by 5,
# print "FizzBuzz" if divisible by both 3 and 5,
# otherwise print the number itself.

fizzy = int(input("Enter a number. "))
if fizzy / 3 and fizzy / 5:
    print("FizzBuzz")
elif fizzy / 3:
    print("Fizz")
elif fizzy / 5:
    print("Buzz")
else: 
    print(fizzy)

print("Fizzy determination complete.")

# Problem 4
# Ask for age and height.
# If age is at least 10 AND height is at least 120 cm, print "You can ride!"
# Otherwise, print "Sorry, you can't ride."

age = int(input("How old are you? "))
height = int(input("How tall are you in centimeters? "))
if age > 10 and height >= 120:
    print("You can ride!")
else:
    print("Sorry, you can't ride.")

print("Age and height determination complete.")

# Problem 5
# Ask the user for a number.
# If it's divisible by 3 AND (either less than 0 OR greater than 100), print "Weird number!"
# Otherwise, print "Normal number."

