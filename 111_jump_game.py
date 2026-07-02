def can_jump(nums):
    reachable = 0
    for i, n in enumerate(nums):
        if i > reachable:
            return False
        reachable = max(reachable, i + n)
    return True

if __name__ == "__main__":
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))
