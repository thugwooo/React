def board2table(m,n,board):
    table = []
    for i in range(n):
        table.append(board[i])


def crash(board):
    return 1


def solution(m,n,board):
    table = board2table(m,n,board)
    count =0

    crash(board)
    return count