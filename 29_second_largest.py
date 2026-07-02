def second_largest(arr):
    first = second = float("-inf")
    for x in arr:
        if x > first:
            first, second = x, first
        elif first > x > second:
            second = x
    return second

if __name__ == "__main__":
    print(second_largest([10, 5, 20, 8, 20]))
