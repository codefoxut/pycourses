

class KnightsTour:

    def __init__(self, n, start_at_center=False):
        self.board_size = n
        self.knights_moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, -1), (-2, 1), (-1, -2), (-1, 2)]
        self.board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.start_at_center = start_at_center

    def display_board(self):
        for i in self.board:
            print(" ".join([str(j).center(4) for j in i]))

    def knights_tour(self):
        if self.start_at_center:
            self.board[self.board_size // 2][self.board_size // 2] = 0
        else:
            self.board[0][0] = 0
        if self.solve(0, 0, 1):
            self.display_board()
        else:
            print("there is no feasible solution to the given problem.")

    def solve(self, x_pos, y_pos, index_order):
        # terminating condition
        if index_order >= self.board_size * self.board_size:
            return True

        for pos in self.knights_moves:
            x_next = x_pos + pos[0]
            y_next = y_pos + pos[1]
            if self.is_valid_move(x_next, y_next):
                self.board[x_next][y_next] = index_order

                if self.solve(x_next, y_next, index_order + 1):
                    return True

                # backTrack
                self.board[x_pos + pos[0]][y_pos + pos[1]] = -1
        return  False

    def is_valid_move(self, x_pos, y_pos):
        if x_pos < 0 or x_pos >= self.board_size:
            return False
        if y_pos < 0 or y_pos >= self.board_size:
            return False
        if self.board[x_pos][y_pos] > -1:
            return False
        return True


if __name__ == '__main__':
    kt = KnightsTour(6)
    kt.display_board()
    print("Knight tour solution")
    kt.knights_tour()
