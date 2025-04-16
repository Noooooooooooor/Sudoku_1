def check_end(board, solution, max_strikes, strikes):
    if strikes >= max_strikes:
        return 'Lost'
    elif np.array_equal(board, solution):
        return 'Won'
    else:
        return 'In Progress'
