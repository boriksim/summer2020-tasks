# 2020-06-11
# Рекурсия


def n_to_one(n):
    print(n)
    if n > 1:
        n_to_one(n - 1)


def one_to_n(n):
    if n > 1:
        one_to_n(n - 1)
    print(n)


def digits_to_left(num):
    if num > 0:
        print(num % 10)
        digits_to_left(num // 10)


def digits_to_right(num):
    if num > 0:
        digits_to_right(num // 10)
        print(num % 10)


def digits_sum(num):
    if num > 0:
        return (num % 10) + digits_sum(num // 10)
    return 0


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1


def fib(max, a=0, b=1):
    if a + b <= max:
        print(a + b)
        fib(max, b, a + b)


def fib_sum(max, a=0, b=1):
    if a + b <= max:
        return a + b + fib_sum(max, b, a + b)
    return 0


def is_palindrome(string):
    if len(string) <= 2:
        return string[0] == string[-1]
    return string[0] == string[-1] and is_palindrome(string[1:-1])


# n_to_one(30)
# one_to_n(30)
# digits_to_left(248)
# digits_to_right(248)
# print(digits_sum(248))
# print(factorial(3))
# fib(8)
# print("sum: ", fib_sum(8))
# print(is_palindrome("ABVBA"))
