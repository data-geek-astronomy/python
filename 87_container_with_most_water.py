def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
