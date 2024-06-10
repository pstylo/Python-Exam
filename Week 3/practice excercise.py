"""Exercise 1: Odd or Even
Write a program that checks whether a given number is odd or even."""

number = int(input("Enter a number: "))

if number % 2 ==0:
    print("The number is even")
else:
    print("The number is odd")

"""Exercise 2: Sum of Numbers
Write a program that calculates the sum of all numbers from 1 to n (where n is a positive integer)."""

n =int(input("Enter a number: "))

sum_numbers = 0
for i in range(1, n+1):
    sum_numbers += i
    print(f"The sum of all numbers from 1 to {n} is {sum_numbers}")