def summary_ranges(nums):
    if not nums:
        return []
    result = []
    start = nums[0]
    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i] != nums[i - 1] + 1:
            end = nums[i - 1]
            result.append(f"{start}" if start == end else f"{start}->{end}")
            if i < len(nums):
                start = nums[i]
    return result

if __name__ == "__main__":
    print(summary_ranges([0, 1, 2, 4, 5, 7]))
