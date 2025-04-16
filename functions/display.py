def display_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            end_char = "\n" if j == 8 else " "
            print(board[i][j], end=end_char)
