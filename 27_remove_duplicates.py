def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
