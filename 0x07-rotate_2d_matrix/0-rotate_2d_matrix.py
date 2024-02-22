def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: List of lists representing the 2D matrix.

    Returns:
    - None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix in-place
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row in-place
    for row in matrix:
        row.reverse()
