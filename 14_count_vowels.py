def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

if __name__ == "__main__":
    print(count_vowels("Aravind Kumar"))
