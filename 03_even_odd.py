def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    for n in range(1, 6):
        print(n, "even" if is_even(n) else "odd")
