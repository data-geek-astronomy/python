def subsets(nums):
    result = [[]]
    for n in nums:
        result += [subset + [n] for subset in result]
    return result

if __name__ == "__main__":
    print(subsets([1, 2, 3]))
