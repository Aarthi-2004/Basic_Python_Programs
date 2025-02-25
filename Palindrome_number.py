To find palindrome number:
def is_palindrome(x):  # fuction defition
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        last_digit = x % 10 # gets the last digit of the number
        reversed_num = reversed_num * 10 + last_digit 
        x = x // 10
    return original == reversed_num

# callling and printing the function
print(is_palindrome(121))  # Output: True
