# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_prime_numbers(numbers):
    """Returns a list of prime numbers from the given list."""
    return [num for num in numbers if is_prime(num)]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [10, 15, 3, 7, 9, 11, 18]
    prime_numbers = filter_prime_numbers(numbers)
    print(prime_numbers)  # Output: [3, 7, 11]

