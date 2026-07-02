def permutations(nums):
    if len(nums) <= 1:
        return [nums]
    result = []
    for i, n in enumerate(nums):
        rest = nums[:i] + nums[i + 1:]
        for perm in permutations(rest):
            result.append([n] + perm)
    return result

if __name__ == "__main__":
    print(permutations([1, 2, 3]))
