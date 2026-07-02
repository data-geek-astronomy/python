def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

if __name__ == "__main__":
    print(rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
