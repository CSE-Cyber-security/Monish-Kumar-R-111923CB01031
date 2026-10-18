
# Fibonacci Series Program

def fibonacci_series(n):
    first = 0
    second = 1

    for i in range(n):
        print(first, end=" ")

        # Calculate the next Fibonacci number
        next_number = first + second

        # Update the values
        first = second
        second = next_number

    print()


# Main program
print("Fibonacci Series")
print("----------------")

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("The Fibonacci series is:")
    fibonacci_series(n)
