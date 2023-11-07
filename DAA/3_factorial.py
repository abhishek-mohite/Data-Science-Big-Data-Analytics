print("iterative algorithm")
def factorial_iterative(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
n = 5
result = factorial_iterative(n)
if result is not None:
    print(f"The factorial of {n} is {result}")
else:
    print("Factorial is not defined for negative numbers")

#recursive algorithm starts
print("recusive algorithm")
def factorial_recursive(n):
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
n = 5
result = factorial_recursive(n)
if result is not None:
    print(f"The factorial of {n} is {result}")
else:
    print("Factorial is not defined for negative numbers")
