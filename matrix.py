import numpy as np

def add_matrices(matrix1, matrix2):
    return np.add(matrix1, matrix2)

def subtract_matrices(matrix1, matrix2):
    return np.subtract(matrix1, matrix2)

def multiply_matrices(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

def transpose_matrix(matrix):
    return np.transpose(matrix)

def main():
    # Get matrix dimensions from user
    rows1 = int(input("Enter number of rows for matrix 1: "))
    cols1 = int(input("Enter number of columns for matrix 1: "))
    rows2 = int(input("Enter number of rows for matrix 2: "))
    cols2 = int(input("Enter number of columns for matrix 2: "))

    # Get matrix elements from user
    matrix1 = []
    for i in range(rows1):
        row = []
        for j in range(cols1):
            row.append(int(input(f"Enter element [{i+1}][{j+1}] for matrix 1: ")))
        matrix1.append(row)

    matrix2 = []
    for i in range(rows2):
        row = []
        for j in range(cols2):
            row.append(int(input(f"Enter element [{i+1}][{j+1}] for matrix 2: ")))
        matrix2.append(row)

    # Convert input lists to numpy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Display input matrices
    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)

    # Get operation choice from user
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    choice = int(input("Enter your choice (1/2/3/4): "))

    # Perform chosen operation
    if choice == 1:
        result = add_matrices(matrix1, matrix2)
        print("Result of addition:")
        print(result)
    elif choice == 2:
        result = subtract_matrices(matrix1, matrix2)
        print("Result of subtraction:")
        print(result)
    elif choice == 3:
        if cols1 != rows2:
            print("Error: Matrices cannot be multiplied.")
        else:
            result = multiply_matrices(matrix1, matrix2)
            print("Result of multiplication:")
            print(result)
    elif choice == 4:
        result1 = transpose_matrix(matrix1)
        result2 = transpose_matrix(matrix2)
        print("Transpose of matrix 1:")
        print(result1)
        print("Transpose of matrix 2:")
        print(result2)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()