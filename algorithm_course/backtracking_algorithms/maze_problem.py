
class MazeProblem:

    def __init__(self, maze_table):
        self.maze_size = len(maze_table)
        self.maze_table = maze_table
        self.solution_table = [[0] * self.maze_size for _ in range(self.maze_size)]

    def solve_maze(self):
        self.solution_table[0][0] = 1
        if self.solve(0, 0):
            self.display_result()
        else:
            print("No feasible solution has found...")

    def display_result(self):
        print("Solution of maze problem.")
        for i in range(self.maze_size):
            for j in range(self.maze_size):
                item = str(self.maze_table[i][j]) if self.solution_table[i][j] == 0 else '*'
                print(item, end=' ')
            print("")

    def solve(self, x_pos, y_pos):
        if (x_pos, y_pos) == (self.maze_size - 1, self.maze_size - 1):
            return True

        for mov in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x_next = x_pos + mov[0]
            y_next = y_pos + mov[1]
            if self.is_feasible(x_next, y_next):
                self.solution_table[x_next][y_next] = 1

                if self.solve(x_next, y_next):
                    return True

                # backTrack
                self.solution_table[x_next][y_next] = 0
        return False

    def is_feasible(self, x, y):
        if x < 0 or x >= self.maze_size:
            return False
        if y < 0 or y >= self.maze_size:
            return False
        if self.solution_table[x][y] == 1:
            return False
        if self.maze_table[x][y] == 1:
            return False
        return True


if __name__ == '__main__':
    maze = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    mp = MazeProblem(maze)
    mp.solve_maze()