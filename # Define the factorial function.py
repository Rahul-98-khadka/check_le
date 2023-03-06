# Define the factorial function
def factorial(n):
    # If the number is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    
    # For other numbers, calculate the factorial using a loop
    fact = 1
    for i in range(2, n+1):
        fact *= i
    
    return fact

num = int(input("Enter a number to find its factorial: "))

print("The factorial of", num, "is", factorial(num))
