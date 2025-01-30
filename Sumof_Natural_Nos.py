# Python Program to Find the Sum of Natural Numbers

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number.")
else:
    result = sum_of_natural_numbers(num)
    print(f"Sum of first {num} natural numbers is {result}")
