def reverse_integer(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    reversed_num = int(str(x)[::-1])
    reversed_num *= sign
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num

if __name__ == "__main__":
    print(reverse_integer(123))
    print(reverse_integer(-123))
