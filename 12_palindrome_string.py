def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome("Racecar"), is_palindrome("hello"))
