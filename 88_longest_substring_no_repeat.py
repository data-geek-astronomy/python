def length_of_longest_substring(s):
    seen = {}
    start = best = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        best = max(best, i - start + 1)
    return best

if __name__ == "__main__":
    print(length_of_longest_substring("abcabcbb"))
