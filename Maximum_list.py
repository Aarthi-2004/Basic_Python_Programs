To find maximum in a list:
def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

# Example usage
print(find_max([1, 2, 3, 4, 5]))  # Output: 5
