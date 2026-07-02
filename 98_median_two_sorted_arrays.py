def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)
    mid = n // 2
    if n % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    return merged[mid]

if __name__ == "__main__":
    print(find_median_sorted_arrays([1, 3], [2]))
    print(find_median_sorted_arrays([1, 2], [3, 4]))
