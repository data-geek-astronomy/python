def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for n in nums:
        for t in range(target, n - 1, -1):
            dp[t] = dp[t] or dp[t - n]
    return dp[target]

if __name__ == "__main__":
    print(can_partition([1, 5, 11, 5]))
    print(can_partition([1, 2, 3, 5]))
