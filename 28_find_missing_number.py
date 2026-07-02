def find_missing(arr, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)

if __name__ == "__main__":
    print(find_missing([1, 2, 4, 5], 5))
