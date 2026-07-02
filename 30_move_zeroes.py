def move_zeroes(arr):
    result = [x for x in arr if x != 0]
    result.extend([0] * (len(arr) - len(result)))
    return result

if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))
