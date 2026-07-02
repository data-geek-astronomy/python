from collections import Counter

def most_common_elements(arr, k):
    return Counter(arr).most_common(k)

if __name__ == "__main__":
    print(most_common_elements([1, 1, 2, 2, 2, 3], 2))
