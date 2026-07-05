def single_number_ii(nums):
    result = 0
    for i in range(32):
        bit_sum = sum((n >> i) & 1 for n in nums)
        if bit_sum % 3:
            result |= (1 << i)
    if result >= 2 ** 31:
        result -= 2 ** 32
    return result

if __name__ == "__main__":
    print(single_number_ii([2, 2, 3, 2]))
