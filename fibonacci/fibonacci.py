def fibonacci_recursive(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_non_recursive(n):
    k = 1
    element = 0
    previous_1 = 1
    previous_2 = 1
    while k < n:
        element = previous_1 + previous_2
        previous_2 = previous_1
        previous_1 = element
        k += 1
    return element


print(fibonacci_recursive(7))
print(fibonacci_non_recursive(7))
