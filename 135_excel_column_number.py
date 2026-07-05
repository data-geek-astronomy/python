def title_to_number(col_title):
    result = 0
    for ch in col_title:
        result = result * 26 + (ord(ch) - ord("A") + 1)
    return result

if __name__ == "__main__":
    print(title_to_number("AB"))
    print(title_to_number("ZY"))
