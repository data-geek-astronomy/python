def fast_power(base, exponent):
    if exponent == 0:
        return 1
    half = fast_power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    return half * half * base

if __name__ == "__main__":
    print(fast_power(2, 10))
