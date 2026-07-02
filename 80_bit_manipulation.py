def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

if __name__ == "__main__":
    print(count_set_bits(29), is_power_of_two(16), is_power_of_two(18))
