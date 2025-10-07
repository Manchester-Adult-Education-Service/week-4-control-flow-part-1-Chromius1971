# -------------------------------------------
# Exercise 1: Boolean Logic
# -------------------------------------------
# In this exercise, you’ll explore how Python uses True and False values.
# Boolean values are either True or False.
# Programs use these values to check conditions and make decisions later.
#
# Examples of Boolean questions:
# - Is this number bigger than that number?
# - Does this word match another word?
# - Did the user enter something?
#
# You’ll practice creating Booleans and printing them to see the results.
# -------------------------------------------

# Step 1: Boolean Basics
# ----------------------
# Booleans can be created by comparing numbers.
# Example: 5 > 3 gives True because 5 is bigger than 3.
# Example: 10 == 8 gives False because 10 is not equal to 8.

# Example of printing a Boolean result:
# print(num1 > num2)  # Prints True or False depending on your numbers

# TODO:
# 1. Create your own two number variables.
# 2. Compare them using >, <, ==, != and print the results.

# Write your code below:
print("Step 1")
print()
num1 = 8
num2 = 49
print("Is number 1 greater than number 2?", num1 > num2)
print("Is number 1 less than number 2?", num1 < num2)
print("Is number 1 equal to number 2?", num1 == num2)
print("This is the opposite of equal to", num1 != num2)
print()

# Step 2: String Comparisons
# --------------------------
# You can compare text (strings) using == or !=.
# Example: "apple" == "apple" gives True.
# Example: "apple" == "Apple" gives False (Python is case-sensitive!).

# Example of printing Boolean results:
# print(word1 == word2)  # Prints True or False depending on your strings

# TODO:
# 1. Create your own two string variables.
# 2. Compare them using == and print the result.
# 3. Compare them using != and print the result.
print("Step 2")
print()
# Write your code below:
dog1 = "Spaniel"
dog2 = "Bulldog"
print()
print("Is dog 1 the same as dog 2?", dog1 == dog2)
print("This is the opposite of the above", dog1 != dog2)
print()
# Step 3: Input and Boolean Results
# ---------------------------------
# You can get input from the user and immediately check something about it.

# Example:
# print(user_number > 10)  # Prints True if number > 10, False otherwise

ID=int(input("Please enter your ID number "))
print("Are the ID numbers the same?", ID == num1)
print()
# TODO:
# 1. Ask the user to enter a number and store it in a variable.
# 2. Compare it to another number and print the Boolean result.
print("Step3")

# Optional:
# Ask the user to type a word and compare it to a stored string, then print True/False.

# Write your code below:

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_boolean.py
#    git commit -m "Completed Boolean logic exercise"
#    git push origin main
# -------------------------------------------

# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Extension 1:
# Ask the user to enter a password.
# Compare it to a stored password and print the Boolean result using print().
# Example:
# print(user_input == stored_password)  # True if correct, False otherwise

# Extension 2:
# Ask the user to enter any text.
# Check if they actually typed something (not empty) and print True/False.
# Example:
# print(len(text_input) > 0)  # True if they typed something

# Extension 3 (more challenging):
# Combine multiple Booleans using AND, OR operators.
# Example idea:
# - Ask the user for two numbers.
# - Check if the first number is greater than 10 AND the second number is less than 20.
# - Print the result.
# Hint: use print((num1 > 10) and (num2 < 20)) to see True or False

# Write your extension code below:


# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex1_boolean.py
#    git commit -m "Completed Boolean extension activities"
#    git push origin main
# Check GitHub to confirm your changes appear.
# -------------------------------------------
