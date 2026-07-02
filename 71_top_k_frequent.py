from collections import Counter

def top_k_frequent(nums, k):
    counts = Counter(nums)
    return [item for item, _ in counts.most_common(k)]

if __name__ == "__main__":
    print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
