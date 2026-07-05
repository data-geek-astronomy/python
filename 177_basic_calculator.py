def calculate(s):
    stack = []
    num = 0
    sign = 1
    result = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            result += sign * num
            num = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif ch == ")":
            result += sign * num
            num = 0
            result *= stack.pop()
            result += stack.pop()
    result += sign * num
    return result

if __name__ == "__main__":
    print(calculate("(1+(4+5+2)-3)+(6+8)"))
