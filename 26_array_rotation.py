def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k] if k else arr

if __name__ == "__main__":
    print(rotate_array([1, 2, 3, 4, 5], 2))
