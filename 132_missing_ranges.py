def find_missing_ranges(nums, lower, upper):
    result = []
    prev = lower - 1
    for n in nums + [upper + 1]:
        if n - prev >= 2:
            result.append((prev + 1, n - 1))
        prev = n
    return result

if __name__ == "__main__":
    print(find_missing_ranges([0, 1, 3, 50, 75], 0, 99))
