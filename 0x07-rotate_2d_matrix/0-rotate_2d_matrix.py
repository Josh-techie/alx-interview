def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix: List of lists representing the 2D matrix.

    Returns:
    - None: The matrix is modified in-place.
    """
    copy_matrix = matrix.copy()
    matrix.clear()

    copy_matrix.reverse()

    for idx in range(len(copy_matrix)):
        temp_row = [element[idx] for element in copy_matrix]
        matrix.append(temp_row)
