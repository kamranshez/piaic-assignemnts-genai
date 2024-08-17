def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def explore_numbers():
    # Get user inputs
    name = input("Enter your name: ")
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
    
    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Store numbers in a list
    numbers = [num1, num2, num3]
    
    # Determine if the numbers are even or odd
    even_odd_info = [(num, "even" if num % 2 == 0 else "odd") for num in numbers]
    
    # Print even/odd information
    for num, type_ in even_odd_info:
        print(f"The number {num} is {type_}.")
    
    # Print each number and its square
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num ** 2})")
    
    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    
    # Print the sum with an encouraging message
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still pretty cool!")

# Run the program
explore_numbers()
