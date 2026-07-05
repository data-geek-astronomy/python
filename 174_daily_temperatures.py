def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    return result

if __name__ == "__main__":
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
