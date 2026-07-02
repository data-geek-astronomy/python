def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

if __name__ == "__main__":
    print(transpose([[1, 2, 3], [4, 5, 6]]))
