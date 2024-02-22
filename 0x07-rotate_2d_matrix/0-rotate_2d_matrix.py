def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: List of lists representing the 2D matrix.

    Returns:
    - None: The matrix is modified in-place.
    """
    # Step 1: Transpose the Matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse Rows
    for row in matrix:
        row.reverse()
