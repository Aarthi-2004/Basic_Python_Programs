To find right triangle star pattern:
def right_triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()

# Example usage
right_triangle(5)
