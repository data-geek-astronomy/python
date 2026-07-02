def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

if __name__ == "__main__":
    print(linear_search([4, 2, 7, 1, 9], 7))
