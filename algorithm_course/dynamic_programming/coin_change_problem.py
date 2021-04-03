
class CoinChange:

    def naive_approach(self, m, value_of_coins, index):

        if m < 0:
            return 0
        if m == 0:
            return 1

        if index == len(value_of_coins):
            return 0

        return self.naive_approach(m-value_of_coins[index], value_of_coins, index) + \
            self.naive_approach(m, value_of_coins, index + 1)

    @staticmethod
    def dynamic_programming_approach(m, value_of_coins):

        # Base conditions.
        dp_table = [[0] * (m + 1) for _ in range(len(value_of_coins) + 1)]

        for i in range(len(value_of_coins) + 1):
            dp_table[i][0] = 1

        for i in range(1, len(value_of_coins) + 1):
            for j in range(1, m + 1):
                if value_of_coins[i - 1] <= j:
                    dp_table[i][j] = dp_table[i - 1][j] + dp_table[i][j - value_of_coins[i - 1]]
                else:
                    dp_table[i][j] = dp_table[i - 1][j]

        print("Solution is: %d" % dp_table[len(value_of_coins)][m])


if __name__ == '__main__':
    m = 1000
    coins = [1, 2, 3]

    CoinChange.dynamic_programming_approach(m, coins)

    soln = CoinChange().naive_approach(m, coins, 0)
    print(soln)



