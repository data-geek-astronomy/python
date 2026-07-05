def add_binary(a, b):
    result = []
    carry = 0
    a, b = a[::-1], b[::-1]
    for i in range(max(len(a), len(b))):
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0
        total = bit_a + bit_b + carry
        result.append(str(total % 2))
        carry = total // 2
    if carry:
        result.append("1")
    return "".join(reversed(result))

if __name__ == "__main__":
    print(add_binary("11", "1"))
