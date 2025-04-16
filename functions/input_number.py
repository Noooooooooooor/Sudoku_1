def input_number(board, number, position):
    row, col = position
    if not (0 <= row < 9 and 0 <= col < 9):
        raise ValueError("Row and column must be between 0 and 8.")
    if not (1 <= number <= 9):
        raise ValueError("Number must be between 1 and 9.")
    if board[row][col] != 0:
        raise ValueError("Cell is already filled.")

    board[row][col] = number
    return board
