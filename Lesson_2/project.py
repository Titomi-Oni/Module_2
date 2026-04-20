#17 April
# Question 1: Print numbers from 1 to 10
for i in range (11):
  print (i)
# Use a loop to print numbers from 1 to 10
# Hint: Use range() starting from 1 and ending at 10
# Print each value inside the loop

# Question 2: Print even numbers from 1 to 20
for i in range (2,21,2):
   print (i)
# Print only even numbers between 1 and 20
# Hint: Use range() with step OR check using if condition
# Print numbers divisible by 2
for i in range (2,21,2):
   print (i)

# Question 3: Multiplication table
num = int(input("Enter a number: "))
for i in range (1,11):
  print(num, "x", i,"=", num * i)
# Take a number as input
# Use loop from 1 to 10
# Print multiplication table in format:
# num x i = result