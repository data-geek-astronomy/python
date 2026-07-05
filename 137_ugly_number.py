def is_ugly(n):
    if n <= 0:
        return False
    for factor in (2, 3, 5):
        while n % factor == 0:
            n //= factor
    return n == 1

if __name__ == "__main__":
    print(is_ugly(6))
    print(is_ugly(14))
