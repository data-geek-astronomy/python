def subarray_sum(nums, k):
    count = 0
    running_sum = 0
    seen = {0: 1}
    for n in nums:
        running_sum += n
        count += seen.get(running_sum - k, 0)
        seen[running_sum] = seen.get(running_sum, 0) + 1
    return count

if __name__ == "__main__":
    print(subarray_sum([1, 1, 1], 2))
    print(subarray_sum([1, 2, 3], 3))
