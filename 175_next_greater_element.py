def next_greater_element(nums1, nums2):
    next_greater = {}
    stack = []
    for n in nums2:
        while stack and stack[-1] < n:
            next_greater[stack.pop()] = n
        stack.append(n)
    return [next_greater.get(n, -1) for n in nums1]

if __name__ == "__main__":
    print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
