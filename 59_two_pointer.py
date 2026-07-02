def is_sorted_pair_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return (arr[left], arr[right])
        elif total < target:
            left += 1
        else:
            right -= 1
    return None

if __name__ == "__main__":
    print(is_sorted_pair_sum([1, 2, 3, 4, 6], 10))
