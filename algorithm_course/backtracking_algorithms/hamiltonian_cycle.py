
class HamiltonianCycle:

    def __init__(self, adjacency_matrix):
        self.n = len(adjacency_matrix)
        self.adjacency_matrix = adjacency_matrix
        self.path = [0]

    def hamiltonian_cycle(self):
        if self.solve(1):
            self.show_hamiltonian_cycle()
        else:
            print("There is no solution to the problem.")

    def solve(self, position):
        # base case
        if position == self.n:

            last_item_index = self.path[position - 1]
            if self.adjacency_matrix[last_item_index][self.path[0]] == 1:
                self.path.append(self.path[0])
                return True
            else:
                return False

        for vertex_index in range(1, self.n):
            if self.is_feasible(vertex_index, position):
                self.path.append(vertex_index)

                if self.solve(position + 1):
                    return True

                # BackTrack
                self.path.pop()
        return False

    def is_feasible(self, vertex, actual_position):

        # check for connection between nodes.
        if self.adjacency_matrix[self.path[actual_position - 1]][vertex] == 0:
            return False

        # whether vertex  already in the list.
        for i in range(actual_position):
            if self.path[i] == vertex:
                return False
        return True

    def show_hamiltonian_cycle(self):
        print(" -> ".join(str(i) for i in self.path))


if __name__ == '__main__':
    m = [
        [0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1],
        [0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0]
    ]
    ham = HamiltonianCycle(m)
    ham.hamiltonian_cycle()