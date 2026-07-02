def is_palindrome_number(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    print(is_palindrome_number(12321), is_palindrome_number(12345))
