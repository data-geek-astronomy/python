def convert_to_title(col_num):
    result = []
    while col_num > 0:
        col_num -= 1
        result.append(chr(col_num % 26 + ord("A")))
        col_num //= 26
    return "".join(reversed(result))

if __name__ == "__main__":
    print(convert_to_title(28))
    print(convert_to_title(701))
