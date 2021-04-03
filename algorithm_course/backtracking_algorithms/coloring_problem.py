
class ColoringProblem:

    def __init__(self, adjacency_matrix, num_colors):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.num_colors = num_colors
        self.colors = [0 for _ in range(self.n)]

    def coloring_problem(self):

        if self.solve(0):
            self.display_result()
        else:
            print("There is no solution possible with given inputs.")

    def solve(self, node_index):

        if node_index == self.n:
            return True

        for color_index in range(1, self.num_colors + 1):
            if self.is_color_valid(node_index, color_index):
                self.colors[node_index] = color_index

                if self.solve(node_index + 1):
                    return True

                # BackTrack step. nothing to remove.
        return False

    def is_color_valid(self, node_index, color_index):

        for i in range(self.n):
            if self.adjacency_matrix[node_index][i] == 1 and self.colors[i] == color_index:
                return False
        return True

    def display_result(self):
        for n, c in zip(range(self.n), self.colors):
            print(f"Node {n} can have color {c}")


if __name__  == '__main__':
    m = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0]
    ]
    color_prob = ColoringProblem(m, 3)
    color_prob.coloring_problem()