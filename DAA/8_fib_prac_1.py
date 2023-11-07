import time
#The provided code demonstrates two methods for 
# computing Fibonacci numbers: a recursive method and a non-recursive (iterative) method.
#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
# typically starting with 0 and 1.
# Recursive Fibonacci
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

# Non-recursive Fibonacci
def non_recursive_fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

# Analyze time and space complexity
def analyze_fibonacci(n):
    # Analyze recursive method
    start_time = time.time()
    recursive_result = recursive_fibonacci(n)
    recursive_time = time.time() - start_time

    # Analyze non-recursive method
    start_time = time.time()
    non_recursive_result = non_recursive_fibonacci(n)
    non_recursive_time = time.time() - start_time

    return {
        "n": n,
        "recursive_result": recursive_result,
        "non_recursive_result": non_recursive_result,
        "recursive_time": recursive_time,
        "non_recursive_time": non_recursive_time,
    }

n = 30  # You can change 'n' to any desired number

analysis = analyze_fibonacci(n)

print(f"Fibonacci({n}) using Recursive: {analysis['recursive_result']} (Time: {analysis['recursive_time']:.6f} seconds)")
print(f"Fibonacci({n}) using Non-Recursive: {analysis['non_recursive_result']} (Time: {analysis['non_recursive_time']:.6f} seconds)")
