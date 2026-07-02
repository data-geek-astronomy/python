def rotate(nums, k):
    n = len(nums)
    k %= n
    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)
    return nums

if __name__ == "__main__":
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
