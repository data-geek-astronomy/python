def add_matrices(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

if __name__ == "__main__":
    print(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
