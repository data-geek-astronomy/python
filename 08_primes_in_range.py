def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    return [n for n in range(start, end + 1) if is_prime(n)]

if __name__ == "__main__":
    print(primes_in_range(1, 50))
