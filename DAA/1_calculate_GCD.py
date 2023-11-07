def calculate_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the GCD
gcd = calculate_gcd(num1, num2)

# Print the result
print(f"The GCD of {num1} and {num2} is {gcd}")
#48,18
#18,12
#12,6
#6

#The Euclidean algorithm efficiently finds the GCD by repeatedly replacing the 
# larger number with the remainder of the division until the remainder becomes zero. 
# The last non-zero remainder is the GC