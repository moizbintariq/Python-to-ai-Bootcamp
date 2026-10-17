def say_hello():
    print("Hello!")
    print("Welcome to Python")

say_hello()


def add(a, b):
    return a + b

print(add(5, 3))
print(add(10, 20))


def square(n):
    return n * n

print(square(6))


def is_even(n):
    if n % 2 == 0:
        return True
    return False

print(is_even(8))
print(is_even(7))


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))


def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_list([1, 2, 3, 4, 5]))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 21):
    if is_prime(num):
        print(num, "is prime")


def find_min_max(numbers):
    return min(numbers), max(numbers)

low, high = find_min_max([4, 8, 1, 9, 3])
print("lowest:", low, "highest:", high)
