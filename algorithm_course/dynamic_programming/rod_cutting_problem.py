
class RodCutting:

    def __init__(self, length_of_rod, prices):
        self.length_of_rod = length_of_rod
        self.prices = prices
        self.dp_table = [[0] * (length_of_rod + 1) for _ in range(len(prices))]

    def dynamic_programming_approach(self):

        for i in range(1, len(self.prices)):
            for j in range(1, self.length_of_rod + 1):
                if i <= j:
                    self.dp_table[i][j] = max(self.dp_table[i - 1][j],
                                              self.prices[i] + self.dp_table[i][j - i])
                else:
                    self.dp_table[i][j] = self.dp_table[i - 1][j]

    def show_result(self):

        print("Max Profit is: $%d" % self.dp_table[len(self.prices) - 1][self.length_of_rod])

        col_index = self.length_of_rod
        row_index = len(self.prices) - 1

        while col_index > 0 or row_index > 0:
            if self.dp_table[row_index][col_index] != self.dp_table[row_index - 1][col_index]:
                print("We cut the rod  for %d" % row_index)
                col_index = col_index - row_index
            else:
                row_index = row_index - 1


if __name__ == '__main__':
    l = 5
    p = [0, 2, 5, 7, 3]
    rc = RodCutting(l, p)
    rc.dynamic_programming_approach()
    rc.show_result()
