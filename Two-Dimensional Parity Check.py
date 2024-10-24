import numpy as np
import matplotlib.pyplot as plt

def calculate_parity(matrix):
    row_parity = np.mod(np.sum(matrix, axis=1), 2)
    column_parity = np.mod(np.sum(matrix, axis=0), 2)
    overall_parity = np.mod(np.sum(row_parity), 2)
    
    return row_parity, column_parity, overall_parity

def plot_parity_matrix(matrix, row_parity, column_parity, overall_parity):
    fig, ax = plt.subplots()
    ax.matshow(matrix, cmap='binary')

    for (i, j), val in np.ndenumerate(matrix):
        ax.text(j, i, f'{val}', ha='center', va='center', color='#fd7f20')

    for i, val in enumerate(row_parity):
        ax.text(matrix.shape[1], i, f'{val}', ha='center', va='center', color='#fc2e20')

    for j, val in enumerate(column_parity):
        ax.text(j, matrix.shape[0], f'{val}', ha='center', va='center', color='#fc2e20')

    ax.text(matrix.shape[1], matrix.shape[0], f'{overall_parity}', ha='center', va='center', color='#fdb750')

    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = np.zeros((rows, cols), dtype=int)
    print("Enter the matrix values (0s and 1s only):")
    for i in range(rows):
        matrix[i] = list(map(int, input(f"Row {i+1}: ").split()))

    print("Matrix:")
    print(matrix)

    row_parity, column_parity, overall_parity = calculate_parity(matrix)

    print("Row Parities: ", row_parity)
    print("Column Parities: ", column_parity)
    print("Overall Parity: ", overall_parity)

    plot_parity_matrix(matrix, row_parity, column_parity, overall_parity)

