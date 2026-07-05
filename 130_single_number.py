def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result

if __name__ == "__main__":
    print(single_number([4, 1, 2, 1, 2]))
