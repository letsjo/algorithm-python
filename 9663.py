# N-Queen
# PyPy3 로 완료

N = int(input())
count = 0
chessBoard = [0] * N
# (x,y) = (index,value)


def checkChessBoard(col):
    for i in range(col):
        if (chessBoard[col] == chessBoard[i] or abs(col-i) == abs(chessBoard[col]-chessBoard[i])):
            return False
    return True


def nQueen(col):
    global count
    if (col == N):
        count += 1
        return

    for row in range(N):
        chessBoard[col] = row
        if (checkChessBoard(col)):
            nQueen(col+1)


nQueen(0)
print(count)
