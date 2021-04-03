

class QueensProblem:

    def __init__(self, n):
        self.n = n
        self.chess_board: list = [[0 for i in range(self.n)] for j in range(self.n)]
        self.backtrack_counnter = 0

    def print_queens(self):
        for i in self.chess_board:
            for j in i:
                if j == 1:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')

    def solve_n_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print("There is no solution to the problem.")

    def solve(self, col_index):

        # terminating condition
        if col_index == self.n:
            return True

        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                # try to place queen on this place.
                self.chess_board[row_index][col_index] = 1
                # progress to next position.
                if self.solve(col_index + 1):
                    return True

                # BackTrack.
                self.backtrack_counnter += 1
                print("Backtrack!! ", col_index, self.backtrack_counnter)
                self.chess_board[row_index][col_index] = None
        return False

    def is_place_valid(self, row, col):
        # check all the rows
        for i in range(self.n):
            if self.chess_board[row][i] == 1:
                return False

        # right diagonal
        j = col
        for x in range(row, -1, -1):
            if x < 0:
                break
            if self.chess_board[x][j] == 1:
                return False
            j -= 1

        # left diagonal
        y = col
        for x in range(row, self.n):
            if y < 0:
                break
            if self.chess_board[x][y] == 1:
                return False
            y -= 1

        return True



if __name__ == '__main__':
    queens_problem = QueensProblem(20)
    queens_problem.solve_n_queens()