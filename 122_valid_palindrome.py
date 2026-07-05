def is_palindrome(s):
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]

if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
    print(is_palindrome("race a car"))
