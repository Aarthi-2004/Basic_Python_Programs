To count vowels in a string:
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        for vowel in vowels:
            if char == vowel:
                count += 1  # increments the count + 1
    return count
print(count_vowels("Hello World"))  # Output: 3
