#Question to swap two variables
Using a temporary variable:
# Python program to swap two variables
x = 5
y = 10
x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

Without Using Temporary Variable:
x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)
