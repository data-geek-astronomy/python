def my_pow(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n:
        if n % 2 == 1:
            result *= x
        x *= x
        n //= 2
    return result

if __name__ == "__main__":
    print(my_pow(2.0, 10))
    print(my_pow(2.0, -2))
